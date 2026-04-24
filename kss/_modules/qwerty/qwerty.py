# Copyright (C) 2021 Hyunwoong Ko <kevin.brain@kakaobrain.com> and Sang Park <sang.park@dnotitia.com>
# All rights reserved.

from functools import partial, lru_cache
from typing import Union, List, Tuple

from kss._modules.qwerty.utils import (
    HANGUL,
    HANGUL_FIRST,
    HANGUL_LAST,
    ENGLISH,
    LEADS,
    VOWELS,
    TAILS,
    CONSONANT_FIRST,
    VOWEL_LAST,
    CONNECTABLE_CONSONANTS,
    CONNECTABLE_VOWELS,
    ENGLISH_INDEX,
    separate_hangul,
    generate_hangul,
    index_of,
    is_vowel,
)
from kss._utils.multiprocessing import _run_job
from kss._utils.sanity_checks import _check_text, _check_type, _check_num_workers


def qwerty(
    text: Union[str, List[str], Tuple[str]],
    src: str,
    tgt: str,
    num_workers: Union[int, str] = "auto",
) -> Union[str, List[str]]:
    """
    This converts text from one language to another using QWERTY keyboard layout.

    Args:
        text (Union[str, List[str], Tuple[str]]): single text or list of texts
        src (str): source language
        tgt (str): target language
        num_workers (Union[int, str]): the number of multiprocessing workers

    Returns:
        Union[str, List[str]]: converted text or list of converted texts

    Examples:
        >>> from kss import Kss
        >>> qwerty = Kss("qwerty")
        >>> text = "dkssudgktpdy"
        >>> qwerty(text, src="en", tgt="ko")
        '안녕하세요'
        >>> text = "안녕하세요"
        >>> qwerty(text, src="ko", tgt="en")
        'dkssudgktpdy'

    References:
        This was copied from [inko.py](https://github.com/738/inko.py) and modified by Kss
    """
    pass


@lru_cache(maxsize=500)
def _qwerty(text, src, tgt):
    pass


def _qwerty_en2ko(text, allow_double_consonant=True):
    def last(_list):
        pass

    def combine(arr):
        def connect(a, b):
            pass

        pass

    def finalize():
        def flush():
            pass

        def transition(char):
            pass

        pass

    pass


def _qwerty_ko2en(text):
    pass
