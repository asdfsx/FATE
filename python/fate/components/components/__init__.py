#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from typing import List


class _ComponentDecorator:
    def __init__(self):
        self._component_map = {}

    def __call__(self, func):
        self._component_map[func.__name__] = func
        return func

    def __getitem__(self, item):
        return self._component_map[item]

    def __contains__(self, item):
        return item in self._component_map

    def __iter__(self):
        return iter(self._component_map)


_lazy_cpn = _ComponentDecorator()


class LazyBuildInComponentsLoader:
    @_lazy_cpn
    def feature_scale(self):
        from .feature_scale import feature_scale

        return feature_scale

    @_lazy_cpn
    def reader(self):
        from .reader import reader

        return reader

    @_lazy_cpn
    def coordinated_lr(self):
        from .coordinated_lr import coordinated_lr

        return coordinated_lr

    @_lazy_cpn
    def coordinated_linr(self):
        from .coordinated_linr import coordinated_linr

        return coordinated_linr

    @_lazy_cpn
    def homo_nn(self):
        from .homo_nn import homo_nn

        return homo_nn

    @_lazy_cpn
    def dataframe_transformer(self):
        from .dataframe_transformer import dataframe_transformer

        return dataframe_transformer

    @_lazy_cpn
    def intersection(self):
        from .intersection import intersection

        return intersection

    @_lazy_cpn
    def evaluation(self):
        from .evaluation import evaluation

        return evaluation

    @_lazy_cpn
    def artifact_test(self):
        from .artifact_test import artifact_test

        return artifact_test

    @_lazy_cpn
    def statistics(self):
        from .statistics import statistics

        return statistics

    @_lazy_cpn
    def dataframe_io_test(self):
        from .dataframe_io_test import dataframe_io_test

        return dataframe_io_test

    @_lazy_cpn
    def multi_model_test(self):
        from .multi_model_test import multi_model_test

        return multi_model_test

    @classmethod
    def contains(cls, cpn_name: str):
        return cpn_name in _lazy_cpn

    @classmethod
    def list(cls) -> List[str]:
        return list(_lazy_cpn)

    def load_cpn(self, cpn_name: str):
        if self.contains(cpn_name):
            return _lazy_cpn[cpn_name](self)
        else:
            raise ValueError(f"Component {cpn_name} does not exist.")
