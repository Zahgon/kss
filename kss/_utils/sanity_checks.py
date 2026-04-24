# Copyright (C) 2021 Hyunwoong Ko <kevin.brain@kakaobrain.com> and Sang Park <sang.park@dnotitia.com>
# All rights reserved.

import numbers
import platform
import unicodedata
from typing import Union, Tuple, List, Any, Optional, Type, Callable, Iterable

from kss._modules.morphemes.analyzers import (
    MecabAnalyzer,
    PecabAnalyzer,
    Analyzer,
    CharacterAnalyzer,
    FastAnalyzer,
)
from kss._utils.logger import logger

MECAB_INFORM, KONLPY_MECAB_INFORM, PECAB_INFORM, FAST_INFORM = (
    False,
    False,
    False,
    False,
)

_mecab_info_linux_macos = "https://github.com/hyunwoongko/python-mecab-kor"
_konlpy_info_linux_macos = "https://konlpy.org/en/latest/api/konlpy.tag/#mecab-class"
_mecab_info_windows = "https://cleancode-ws.tistory.com/97"
_konlpy_info_windows = "https://uwgdqo.tistory.com/363"
_pecab_info = "https://github.com/hyunwoongko/pecab"


def _message_by_user_os(linux_macos: str, windows: str) -> str:
    pass


def _check_value(
    param: Any, param_name: str, predicate: Callable, suggestion: str
) -> Any:
    """
    Check param value

    Args:
        param (bool): param value
        param_name (str): param name
        predicate (Callable): callable
        suggestion (str): suggestion message

    Returns:
        Any: param value
    """
    pass


def _check_iterable_type(
    param: Iterable, param_name: str, iterable_type: Type, element_type: Type
) -> Any:
    """
    Check iterable param type

    Args:
        param (Iterable): iterable param value
        param_name (str): param name
        iterable_type (Type): iterable type
        element_type (Type): element type

    Returns:
        Any: param value
    """
    pass


def _check_type(param: Any, param_name: str, types: Union[Type, List[Type]]) -> Any:
    """
    Check param type

    Args:
        param (bool): param value
        param_name (str): param name
        types (Union[Type, List[Type]]): types

    Returns:
        Any: param value
    """
    pass


def _check_char(text: str) -> str:
    """
    Check text length is 1.

    Args:
        text (str): text

    Returns:
        str: text
    """
    pass


def _check_text(
    text: Union[str, List[str], Tuple[str]]
) -> Tuple[Union[str, List[str], Tuple[str]], bool]:
    """
    Check input text type.

    Args:
        text (Union[str, List[str], Tuple[str]]): single text or list/tuple of texts

    Returns:
        Tuple[Union[str, List[str], Tuple[str]], bool]: single text or list/tuple of texts
            and whether it can finish processing right now or not.
    """
    pass


def _check_analyzer_backend_mecab_pecab_only(backend: str) -> Analyzer:
    pass


def _check_analyzer_backend(backend: str) -> Analyzer:
    """
    Check morpheme analyzer backend type.

    Args:
        backend (str):

    Returns:
        Analyzer: morpheme analyzer backend.
    """
    pass


def _check_num_workers(
    inputs: Any, num_workers: Union[int, str]
) -> Optional[Union[int, bool]]:
    """
    Check the number of multiprocessing workers.

    Args:
        inputs (Any): input data
        num_workers (Union[int, str]): the number of multiprocessing workers

    Returns:
        Optional[Union[int, bool]]: the number of multiprocessing workers.
            `None` means maximum number of workers which can be used for now.
            `False` means that it will not use multiprocessing.
    """
    pass
