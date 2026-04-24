# Copyright (C) 2021 Hyunwoong Ko <kevin.brain@kakaobrain.com> and Sang Park <sang.park@dnotitia.com>
# All rights reserved.

from typing import List, Tuple

try:
    from mecab import MeCab
except Exception:
    pass
try:
    from konlpy.tag import Mecab
except Exception:
    pass
try:
    import MeCab
except Exception:
    pass
try:
    from konlpy.tag import Mecab
except Exception:
    pass
try:
    from pecab import PeCab
except Exception:
    pass


def _get_linux_mecab():
    pass


def _get_linux_konlpy_mecab():
    pass


def _get_windows_mecab():
    def pos(text: str) -> List[Tuple[str, str]]:
        """Mecab MSVC wrapper"""
        pass

    pass


def _get_windows_konlpy_mecab():
    pass


def _get_mecab():
    """
    Try to import and get mecab morpheme analyzer

    Returns:
        Tuple[Optional[Union[mecab.MeCab, konlpy.tag.Mecab, Mecab.Tagger]], Optional[str]]:
            mecab morpheme analyzer and its backend
    """
    pass


def _get_pecab():
    """
    Try to import and get pecab morpheme analyzer

    Returns:
        Tuple[Optional[pecab.PeCab], Optional[str]]:
            pecab morpheme analyzer and its backend
    """
    pass


def _preserve_space(
    text: str,
    tokens: List[Tuple[str, str]],
    spaces: str,
) -> List[Tuple[str, str]]:
    """
    Restore spaces from analyzed results

    Args:
        text (str): input text
        tokens (List[Tuple[str, str]]): analyzed results
        spaces (str): space tokens to add

    Returns:
        List[Tuple[str, str]]: analyzed results with space
    """
    pass


def _reset_spaces(text: str, tokens: List[Tuple[str, str]]):
    pass
