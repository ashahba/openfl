# Copyright 2020-2024 Intel Corporation
# SPDX-License-Identifier: Apache-2.0


"""openfl.federated package."""

from importlib import util

from openfl.federated.data import DataLoader  # NOQA
from openfl.federated.plan import Plan  # NOQA
from openfl.federated.task import TaskRunner  # NOQA

if util.find_spec("tensorflow") is not None:
    from openfl.federated.data import FederatedDataSet  # NOQA
    from openfl.federated.data import KerasDataLoader, TensorFlowDataLoader
    from openfl.federated.task import FederatedModel  # NOQA
    from openfl.federated.task import KerasTaskRunner, TensorFlowTaskRunner
if util.find_spec("torch") is not None:
    from openfl.federated.data import FederatedDataSet  # NOQA
    from openfl.federated.data import PyTorchDataLoader
    from openfl.federated.task import FederatedModel  # NOQA
    from openfl.federated.task import PyTorchTaskRunner
if util.find_spec("xgboost") is not None:
    from openfl.federated.data import FederatedDataSet  # NOQA
    from openfl.federated.data import XGBoostDataLoader
    from openfl.federated.task import FederatedModel  # NOQA
    from openfl.federated.task import XGBoostTaskRunner

__all__ = [
    "Plan",
    "TaskRunner",
    "DataLoader",
]
