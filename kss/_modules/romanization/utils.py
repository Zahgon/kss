# Copyright (C) 2021 Hyunwoong Ko <kevin.brain@kakaobrain.com> and Sang Park <sang.park@dnotitia.com>
# All rights reserved.

import re

from kss._modules.g2p.english import convert_eng
from kss._modules.g2p.numerals import convert_num

unicode_initial = [chr(initial_code) for initial_code in range(4352, 4371)]
unicode_medial = [
    'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ'
]
unicode_final = [chr(final_code) for final_code in range(0x11a8, 0x11c3)]
unicode_final.insert(0, None)
unicode_offset = 44032
unicode_initial_offset = 588
unicode_medial_offset = 28

unicode_compatible_consonants = [
    'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]
unicode_compatible_finals = [
    'ᆨ', 'ᆩ', 'ᆫ', 'ᆮ', '_', 'ᆯ', 'ᆷ', 'ᆸ', '_', 'ᆺ', 'ᆻ', 'ᆼ', 'ᆽ', '_', 'ᆾ', 'ᆿ', 'ᇀ', 'ᇁ', 'ᇂ'
]

double_consonant_final = {
    'ᆪ': ('ᆨ', 'ᆺ'),
    'ᆬ': ('ᆫ', 'ᆽ'),
    'ᆭ': ('ᆫ', 'ᇂ'),
    'ᆰ': ('ᆯ', 'ᆨ'),
    'ᆱ': ('ᆯ', 'ᆷ'),
    'ᆲ': ('ᆯ', 'ᆸ'),
    'ᆳ': ('ᆯ', 'ᆻ'),
    'ᆴ': ('ᆯ', 'ᇀ'),
    'ᆵ': ('ᆯ', 'ᇁ'),
    'ᆶ': ('ᆯ', 'ᇂ'),
    'ᆹ': ('ᆸ', 'ᆺ'),
    'ㅆ': ('ㅅ', 'ㅅ')
}

NULL_CONSONANT = 'ᄋ'


class Syllable(object):
    def __init__(self, char):
        self.char = char
        _is_hangul, _separated = self.separate_syllable(char)
        if _is_hangul:
            self.initial = unicode_initial[_separated[0]]
            self.medial = unicode_medial[_separated[1]]
            self.final = unicode_final[_separated[2]]
        else:
            self.initial = _separated[0]
            self.medial = None
            self.final = None

    def separate_syllable(self, char):
        pass

    def construct_syllable(self, initial, medial, final):
        pass

    @staticmethod
    def is_hangul(char):
        pass

    @staticmethod
    def final_to_initial(char):
        pass

    def __repr__(self):
        self.construct_syllable(self.initial, self.medial, self.final)
        return self.char

    def __str__(self):
        self.char = self.construct_syllable(self.initial, self.medial, self.final)
        return self.char


def pronounce(
    text,
    convert_english_to_hangul_phonemes=False,
    convert_numbers_to_hangul_phonemes=False,
):
    pass
