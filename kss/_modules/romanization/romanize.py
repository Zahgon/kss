# Copyright (C) 2021 Hyunwoong Ko <kevin.brain@kakaobrain.com> and Sang Park <sang.park@dnotitia.com>
# All rights reserved.

# This code was copied from korean-romanizer [https://github.com/osori/korean-romanizer]
# And modified by Hyunwoong Ko [https://github.com/hyunwoongko] and Sohyeon Yim [https://github.com/sohyunwriter]

import re
from functools import partial
from typing import Union, List, Tuple

from unidecode import unidecode

from kss._modules.g2p.g2p import g2p
from kss._modules.romanization.utils import pronounce, Syllable
from kss._utils.multiprocessing import _run_job
from kss._utils.sanity_checks import _check_text, _check_type, _check_num_workers, _check_analyzer_backend_mecab_pecab_only

vowel = {
    # 단모음 monophthongs
    'ㅏ': 'a',
    'ㅓ': 'eo',
    'ㅗ': 'o',
    'ㅜ': 'u',
    'ㅡ': 'eu',
    'ㅣ': 'i',
    'ㅐ': 'ae',
    'ㅔ': 'e',
    'ㅚ': 'oe',
    'ㅟ': 'wi',
    # 이중모음 diphthongs
    'ㅑ': 'ya',
    'ㅕ': 'yeo',
    'ㅛ': 'yo',
    'ㅠ': 'yu',
    'ㅒ': 'yae',
    'ㅖ': 'ye',
    'ㅘ': 'wa',
    'ㅙ': 'wae',
    'ㅝ': 'wo',
    'ㅞ': 'we',
    'ㅢ': 'ui',  # [붙임 1] ‘ㅢ’는 ‘ㅣ’로 소리 나더라도 ‘ui’로 적는다.
}

# 초성 Choseong (Syllable Onset)
onset = {
    # 파열음 stops/plosives
    'ᄀ': 'g',
    'ᄁ': 'kk',
    'ᄏ': 'k',
    'ᄃ': 'd',
    'ᄄ': 'tt',
    'ᄐ': 't',
    'ᄇ': 'b',
    'ᄈ': 'pp',
    'ᄑ': 'p',
    # 파찰음 affricates
    'ᄌ': 'j',
    'ᄍ': 'jj',
    'ᄎ': 'ch',
    # 마찰음 fricatives
    'ᄉ': 's',
    'ᄊ': 'ss',
    'ᄒ': 'h',
    # 비음 nasals
    'ᄂ': 'n',
    'ᄆ': 'm',
    # 유음 liquids
    'ᄅ': 'r',
    # Null sound
    'ᄋ': '',
}

coda = {
    # 파열음 stops/plosives
    'ᆨ': 'k',
    'ᆮ': 't',
    'ᆸ': 'p',
    # 비음 nasals
    'ᆫ': 'n',
    'ᆼ': 'ng',
    'ᆷ': 'm',
    # 유음 liquids
    'ᆯ': 'l',
    None: '',
}


def romanize(
    text: Union[str, List[str], Tuple[str]],
    use_morpheme_info: bool = True,
    backend: str = "auto",
    convert_english_to_hangul_phonemes: bool = False,
    convert_numbers_to_hangul_phonemes: bool = False,
    num_workers: Union[int, str] = "auto",
) -> Union[str, List[str]]:
    """
    This romanizes Korean text.

    Args:
        text (Union[str, List[str], Tuple[str]]): single text or list of texts
        use_morpheme_info (bool): whether to use morpheme information or not
        backend (str): morpheme analyzer backend. 'mecab', 'pecab' are supported
        convert_english_to_hangul_phonemes (bool): whether to convert English to Hangul phonemes or not
        convert_numbers_to_hangul_phonemes (bool): whether to convert numbers to Hangul phonemes or not
        num_workers (Union[int, str]): the number of multiprocessing workers

    Returns:
        Union[str, List[str]]: romanized text or list of romanized texts

    Examples:
        >>> from kss import Kss
        >>> romanize = Kss("romanize")
        >>> text = "안녕하세요"
        >>> romanize(text)
        'annyeonghaseyo'
        >>> text = "대관령"
        >>> romanize(text)
        'daegwallyeong'

    References:
        This was copied from [korean-romanizer](https://github.com/osori/korean-romanizer) and modified by Kss
    """
    pass


def _romanize(
    text,
    use_morpheme_info=True,
    backend="auto",
    convert_english_to_hangul_phonemes=False,
    convert_numbers_to_hangul_phonemes=False,
):
    pass
