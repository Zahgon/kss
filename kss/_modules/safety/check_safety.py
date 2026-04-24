# Copyright (C) 2021 Hyunwoong Ko <kevin.brain@kakaobrain.com> and Sang Park <sang.park@dnotitia.com>
# All rights reserved.

from functools import partial
from typing import Union, List, Tuple

from kss._modules.safety.utils import bad_words, exceptions, pattern
from kss._utils.multiprocessing import _run_job
from kss._utils.sanity_checks import _check_text, _check_num_workers, _check_type


def is_unsafe(
    text: Union[str, List[str], Tuple[str]],
    return_matches: bool = False,
    num_workers: Union[int, str] = "auto",
) -> Union[bool, List[bool], List[bool], List[List[str]]]:
    """
    This checks if the text is unsafe or not.

    Args:
        text (Union[str, List[str], Tuple[str]]): single text or list of texts
        return_matches (bool): whether to return matches or not
        num_workers (Union[int, str]): the number of multiprocessing workers

    Returns:
        Union[bool, List[bool], List[bool], List[List[str]]]:
            whether the text is unsafe or not
            or list of whether the texts are unsafe or not
            or list of matched bad words in the texts

    Examples:
        >>> from kss import Kss
        >>> is_unsafe = Kss("is_unsafe")
        >>> text = "안녕하세요"
        >>> is_unsafe(text)
        False
        >>> text = "안녕하세요. 씨발"
        >>> is_unsafe(text)
        True
        >>> text = ["안녕하세요", "안녕하세요. 씨발"]
        >>> is_unsafe(text)
        [False, True]
        >>> text = "안녕하세요. 씨발"
        >>> is_unsafe(text, return_matches=True)
        ['씨발']
        >>> text = ["안녕하세요", "안녕하세요. 씨발"]
        >>> is_unsafe(text, return_matches=True)
        [[], ['씨발']]
    """
    pass


def _is_unsafe(text: str, return_matches: bool = False):
    pass


def _is_unsafe_regex(text: str, return_matches: bool = False):
    pass


def _is_unsafe_dict(text: str, return_matches: bool = False):
    pass
