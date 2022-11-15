import copy

import pandas as pd
import numpy as np
import torch
import operator


# TODO: record data type, support multiple data types
class DataFrame(object):
    def __init__(self,
                 ctx,
                 schema,
                 index=None,
                 match_id=None,
                 values=None,
                 label=None,
                 weight=None):
        self._ctx = ctx
        self._index = index
        self._match_id = match_id
        self._values = values
        self._label = label
        self._weight = weight
        self._schema = schema

        self.__shape = None
        self._columns = None

        self._tensor_label = None

    @property
    def index(self):
        return self._index

    @property
    def values(self):
        return self._values

    @property
    def label(self):
        return self._label

    @property
    def weight(self):
        return self._weight

    @property
    def match_id(self):
        return self._match_id

    @property
    def shape(self):
        if self.__shape:
            return self.__shape

        if self._values is None:
            self.__shape = (self._index.count(), 0)
        else:
            self.__shape = (self._index.count(), len(self._schema["header"]))

        return self.__shape

    @property
    def schema(self) -> dict:
        return self._schema

    @property
    def columns(self) -> "ColumnObject":
        if not self._columns:
            self._columns = ColumnObject(self._schema["header"])
        else:
            return self._columns

    def max(self, *args, **kwargs) -> "DataFrame":
        max_ret = self._values.max(*args, **kwargs)
        return self._process_stat_func(max_ret, *args, **kwargs)

    def min(self, *args, **kwargs) -> "DataFrame":
        min_ret = self._values.min(*args, **kwargs)
        return self._process_stat_func(min_ret, *args, **kwargs)

    def mean(self, *args, **kwargs) -> "DataFrame":
        mean_ret = self._values.mean(*args, **kwargs)
        return self._process_stat_func(mean_ret, *args, **kwargs)

    def sum(self, *args, **kwargs) -> "DataFrame":
        sum_ret = self._values.sum(*args, **kwargs)
        return self._process_stat_func(sum_ret, *args, **kwargs)

    def std(self, *args, **kwargs) -> "DataFrame":
        std_ret = self._values.std(*args, **kwargs)
        return self._process_stat_func(std_ret, *args, **kwargs)

    def count(self) -> "int":
        return self.shape[0]

    def _process_stat_func(self, stat_ret, *args, **kwargs) -> "pd.Series":
        if not kwargs.get("axis", 0):
            return pd.Series(stat_ret, index=self._schema["header"])
        else:
            return pd.Series(stat_ret)

    def __add__(self, other):
        return self._arithmetic_operate(operator.add, other)

    def __sub__(self, other):
        return self._arithmetic_operate(operator.sub, other)

    def __mul__(self, other):
        return self._arithmetic_operate(operator.mul, other)

    def __truediv__(self, other):
        return self._arithmetic_operate(operator.truediv, other)

    def _arithmetic_operate(self, op, other):
        if isinstance(other, pd.Series):
            other = torch.tensor(pd.Series)
        elif isinstance(other, DataFrame):
            other = other.values
        elif isinstance(other, (int, float, np.int, np.int32, np.int64, np.float, np.float32, np.float64)):
            pass
        else:
            raise ValueError(f"{op.__name__} between {DataFrame} and {type(other)} is not supported")

        ret_value = op(self._values, other.values)
        return DataFrame(self._ctx, index=self._index, values=ret_value, label=self._label, weight=self._weight,
                         schema=self._schema)

    def __getitem__(self, items):
        indexes = self.__get_index_by_column_names(items)
        ret_tensor = self._values[:, indexes]

        header_mapping = dict(zip(self._schema["header"], range(len(self._schema["header"]))))
        new_schema = copy.deepcopy(self._schema)
        new_header = items if isinstance(items, list) else [items]
        new_anonymous_header = []

        for item in items:
            index = header_mapping[item]
            new_anonymous_header.append(self._schema["anonymous_header"][index])

        new_schema["header"] = new_header
        new_schema["anonymous__header"] = new_anonymous_header

        return DataFrame(self._ctx, index=self._index, values=ret_tensor, label=self._label, weight=self._weight,
                         schema=new_schema)

    def __setitem__(self, keys, item):
        if not isinstance(item, DataFrame):
            raise ValueError("Using syntax df[[col1, col2...]] = rhs, rhs should be a dataframe")

        indexes = self.__get_index_by_column_names(keys)
        self._values[:, indexes] = item._values

        return self

    def __len__(self):
        return self.count()

    def __get_index_by_column_names(self, column_names):
        if isinstance(column_names, str):
            column_names = [column_names]

        indexes = []
        header_mapping = dict(zip(self._schema["header"], range(len(self._schema["header"]))))
        for col in column_names:
            index = header_mapping.get(col, None)
            if index is None:
                raise ValueError(f"Can not find column: {col}")
            indexes.append(index)

        return indexes

    def loc(self, ids):
        # this is very costly, use iloc is better
        # TODO: if data is not balance, repartition is need?
        if not isinstance(ids, (int, list)):
            raise ValueError(f"loc function accepts single id or list of ids, but {ids} found")

        if isinstance(ids, int):
            ids = [ids]

        indexes = self._index.get_indexer(ids)

        return self.iloc(indexes)

    def iloc(self, indexes):
        # TODO: if data is not balance, repartition is need?
        if not isinstance(indexes, (int, list)):
            raise ValueError(f"iloc function accepts single integer or list of integers, but {indexes} found")

        weight = self._weight[indexes] if self._weight else None
        label = self._label[indexes] if self._label else None
        values = self._values[indexes] if self._values else None
        match_id = self._match_id[indexes] if self._match_id else None
        index = self._index[indexes] if self._index else None

        return DataFrame(
            self._ctx,
            self._schema,
            index=index,
            match_id=match_id,
            label=label,
            weight=weight,
            values=values
        )

    def to_local(self):
        ret_dict = {
            "index": self._index.to_local(),
        }
        if self._values:
            ret_dict["values"] = self._values.to_local()
        if self._weight:
            ret_dict["weight"] = self._weight.to_local()
        if self._label:
            ret_dict["label"] = self._label.to_local()
        if self._match_id:
            ret_dict["match_id"] = self._match_id.to_local()

        return DataFrame(
            self._ctx,
            self._schema,
            **ret_dict
        )

    def serialize(self):
        """
        this function change tensor to a normal distributed table
        """

    def deserialize(self):
        """
        this function change a distributed table to tensor
        """
        ...


class ColumnObject(object):
    def __init__(self, col_names):
        self._col_names = col_names

    def __getitem__(self, items):
        if isinstance(items, int):
            return self._col_names[items]
        else:
            ret_cols = []
            for item in items:
                ret_cols.append(self._col_names[item])

            return ColumnObject(ret_cols)

    def tolist(self):
        return self._col_names

    def __iter__(self):
        return (col_name for col_name in self._col_names)

