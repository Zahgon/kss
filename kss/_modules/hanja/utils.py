# -*- coding:utf-8 -*-
# Copyright (C) 2021 Hyunwoong Ko <kevin.brain@kakaobrain.com> and Sang Park <sang.park@dnotitia.com>
# All rights reserved.

# This was copied from [hanja](https://github.com/suminb/hanja) and modified by Kss

import os

import yaml


def load_table(filename):
    """Loads the Hanja table."""
    pass


try:
    basepath = os.path.abspath(os.path.dirname(__file__))
    hanja_table = load_table(os.path.join(basepath, "assets", "table.yml"))
except Exception:
    basepath = None
    hanja_table = None


def separate(ch):
    """한글 자모 분리. 주어진 한글 한 글자의 초성, 중성 초성을 반환함."""
    pass


def synthesize(choseong, joongseong, jongseong):
    pass


def build(choseong, joongseong, jongseong):
    """초성, 중성, 종성을 조합하여 완성형 한 글자를 만듦. 'choseong',
    'joongseong', 'jongseong' are offsets. For example, 'ㄱ' is 0, 'ㄲ' is 1,
    'ㄴ' is 2, and so on and so fourth."""
    pass


def dooeum(previous, current):
    """두음법칙을 적용하기 위한 함수."""
    pass


def is_hangul(ch):
    pass


def contains_hangul(text):
    pass


def translate_syllable(previous, current):
    """Translates a single syllable."""
    pass


def _split_hanja(text):
    """주어진 문장을 한자로 된 구역과 그 이외의 문자로 된 구역으로 분리"""
    pass


def split_hanja(text):
    """Splits a given text into hanja and non-hanja parts."""
    pass


def get_format_string(mode, word):
    """
    :param mode: substitution | combination-text | combination-text-reversed | combination-html | combination-html-reversed
    """
    pass


def translate(text, mode):
    """Translates entire text."""
    pass


def translate_word(word, prev, format_string):
    """Translates a single word.

    :param word: Word to be translated
    :param prev: Preceeding word
    """
    pass


def is_hanja(ch):
    """Determines if a given character ``ch`` is a Chinese character."""
    pass
