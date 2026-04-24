# Copyright (C) 2021 Hyunwoong Ko <kevin.brain@kakaobrain.com> and Sang Park <sang.park@dnotitia.com>
# All rights reserved.

# This code was copied from g2pk [https://github.com/kyubyong/g2pK]
# And modified by Hyunwoong Ko [https://github.com/hyunwoongko]

import os
import re

import cmudict

import kss
from kss._modules.jamo._jamo import h2j, j2h


def adjust(arpabets):
    """Modify arpabets so that it fits our processes"""
    pass


def to_choseong(arpabet):
    """Arpabet to choseong or onset"""
    pass


def to_jungseong(arpabet):
    """Arpabet to jungseong or vowel"""
    pass


def to_jongseong(arpabet):
    """Arpabet to jongseong or coda"""
    pass


def reconstruct(string):
    """Some postprocessing rules"""
    pass


def parse_table():
    """Parse the main rule table"""
    pass


def annotate(string, backend):
    """attach pos tags to the given string using Mecab"""
    pass


def group(inp):
    """For group_vowels=True
    Contemporarily, Korean speakers don't distinguish some vowels.
    """
    pass


def _get_examples():
    """For internal use"""
    pass


def get_rule_id2text():
    """for verbose=True"""
    pass


def get_idioms():
    pass


def gloss(verbose, out, inp, rule):
    """displays the process and relevant information"""
    pass


def convert_idioms(
    text,
    descriptive=False,
    convert_english_to_hangul_phonemes=True,
    convert_numbers_to_hangul_phonemes=True,
    verbose=False,
):
    """Process each line in `idioms.txt`
    Each line is delimited by "===",
    and the left string is replaced by the right one.
    inp: input string.
    descriptive: not used.
    verbose: boolean.

    >>> convert_idioms("지금 mp3 파일을 다운받고 있어요")
    지금 엠피쓰리 파일을 다운받고 있어요
    """
    pass


try:
    cmu = cmudict.dict()
    rule_id2text = get_rule_id2text()
    idioms = get_idioms()
    table = parse_table()
except Exception:
    cmu = None
    idioms = None
    rule_id2text = None
    table = None
