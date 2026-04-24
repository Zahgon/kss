# Copyright (C) 2021 Hyunwoong Ko <kevin.brain@kakaobrain.com> and Sang Park <sang.park@dnotitia.com>
# All rights reserved.


import multiprocessing as mp
from typing import Union, Any, List, Optional, Callable


def _run_job(
    func: Callable,
    inputs: Any,
    num_workers: Optional[Union[int, bool]] = None,
) -> Union[Any, List[Any]]:
    """
    Run job with or without multiprocessing.

    Args:
        func (Callable): function to run
        inputs (Any): input data
        num_workers (Optional[Union[int, bool]]): the number of multiprocessing workers.

    Returns:
        Union[Any, List[Any]]: output of the job.
    """
    pass
