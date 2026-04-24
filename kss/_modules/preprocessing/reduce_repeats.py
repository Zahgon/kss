# Copyright (C) 2021 Hyunwoong Ko <kevin.brain@kakaobrain.com> and Sang Park <sang.park@dnotitia.com>
# All rights reserved.

# This code was copied from [soynlp](https://github.com/lovit/soynlp)
# And modified by Hyunwoong Ko [https://github.com/hyunwoongko]

import re
from functools import partial
from typing import List, Tuple, Union

from kss._utils.multiprocessing import _run_job
from kss._utils.sanity_checks import _check_num_workers, _check_text, _check_type

kor_begin = 44032
kor_end = 55203
chosung_base = 588
jungsung_base = 28
jaum_begin = 12593
jaum_end = 12622
moum_begin = 12623
moum_end = 12643

chosung_list = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ',
                'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
jungsung_list = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ',
                 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ',
                 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ',
                 'ㅡ', 'ㅢ', 'ㅣ']
jongsung_list = [
    ' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ',
    'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ',
    'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ',
    'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
jaum_list = ['ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄸ', 'ㄹ',
             'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ',
             'ㅃ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
moum_list = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ',
             'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']

repeatchars_pattern = re.compile('(\w)\\1{2,}')


def _compose(chosung, jungsung, jongsung):
    pass


def _decompose(c):
    pass


def _is_hangul(c):
    pass


def _is_composed_hangul(c):
    pass


def _is_consonant(c):
    pass


def _is_vowel(c):
    pass


def _to_base(c):
    pass


def _character_is_number(i):
    pass


def _character_is_english(i):
    pass


def _character_is_punctuation(i):
    pass


def reduce_char_repeats(
    text: Union[str, List[str], Tuple[str]],
    num_repeats: int = 2,
    num_workers: Union[int, str] = "auto",
) -> Union[str, List[str]]:
    """
    This reduces character repeats in text.

    Args:
        text (Union[str, List[str], Tuple[str]]): single text or list of texts
        num_repeats (int): the number of character that can be repeated
        num_workers (Union[int, str]): the number of multiprocessing workers

    Returns:
        Union[str, List[str]]: text with reduced character repeats or list of texts with reduced character repeats

    Examples:
        >>> from kss import Kss
        >>> reduce_char_repeats = Kss("reduce_char_repeats")
        >>> text = "고고고고고고고"
        >>> output = reduce_char_repeats(text)
        >>> print(output)
        '고고'

    References:
        This was copied from [soynlp](https://github.com/lovit/soynlp) and modified by Kss
    """
    pass


def reduce_emoticon_repeats(
    text: Union[str, List[str], Tuple[str]],
    num_repeats: int = 2,
    num_workers: Union[int, str] = "auto",
) -> Union[str, List[str]]:
    """
    This reduces emoticon repeats in text.

    Args:
        text (Union[str, List[str], Tuple[str]]): single text or list of texts
        num_repeats (int): the number of emoticon that can be repeated
        num_workers (Union[int, str]): the number of multiprocessing workers

    Returns:
        Union[str, List[str]]: text with reduced emoticon repeats or list of texts with reduced emoticon repeats

    Examples:
        >>> from kss import Kss
        >>> reduce_emoticon_repeats = Kss("reduce_emoticon_repeats")
        >>> text = "앜ㅋㅋㅋㅋㅋㅋ"
        >>> output = reduce_emoticon_repeats(text)
        >>> print(output)
        '아ㅋㅋ'

    References:
        This was copied from [soynlp](https://github.com/lovit/soynlp) and modified by Kss
    """
    pass


def _reduce_char_repeats(sent, num_repeats=2):
    pass


def _reduce_emoticon_repeats(sent, num_repeats=2):
    def pattern(idx):
        pass

    pass
