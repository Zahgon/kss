# Copyright (C) 2021 Hyunwoong Ko <kevin.brain@kakaobrain.com> and Sang Park <sang.park@dnotitia.com>
# All rights reserved.

import multiprocessing as mp
from typing import Callable, Any, Optional, Union, List, Tuple

import tossi

from kss._modules.morphemes.split_morphemes import split_morphemes


def _check_text(
    param_1: Union[str, List[str]],
    param_2: Union[str, List[str]],
    param_1_name: str,
    param_2_name: str
) -> Tuple[Union[str, List[str]], Union[str, List[str]]]:
    pass


def _run_job(
    func: Callable,
    input_1: List[str],
    input_2: List[str],
    input_1_name: str,
    input_2_name: str,
    num_workers: Optional[Union[int, bool]] = None,
) -> Union[Any, List[Any]]:
    """
    Run job with or without multiprocessing.

    Args:
        func (Callable): function to run
        input_1 (List[str]): input data
        input_2 (List[str]): input data
        input_1_name (str): input data name
        input_2_name (str): input data name
        num_workers (Optional[Union[int, bool]]): the number of multiprocessing workers.
    """
    pass


def _check_num_workers(
    param_1: List[str],
    param_2: List[str],
    param_1_name: str,
    param_2_name: str,
    num_workers: Union[int, str],
) -> Optional[Union[int, bool]]:
    pass


def _preprocess_josa(prefix, josa):
    pass


def _select_josa(prefix, josa):
    pass


def _combine_josa(prefix, josa):
    pass
