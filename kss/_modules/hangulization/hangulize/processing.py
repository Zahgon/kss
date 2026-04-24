# -*- coding: utf-8 -*-
"""
    hangulize.processing
    ~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2010-2017 by Heungsub Lee
    :license: BSD, see LICENSE for more details.
"""
from __future__ import absolute_import

from kss._modules.hangulization.hangulize.hangul import EU, Null, NG, UnicodeHangulError, join, split
from kss._modules.hangulization.hangulize.models import Choseong, Impurity, Jongseong, Jungseong


__all__ = ['complete_syllable', 'complete_syllables', 'split_phonemes',
           'join_phonemes']


def complete_syllable(syllable):
    """Inserts the default jungseong or jongseong if it is not exists::

        >>> complete_syllable((Jungseong(YO),))
        (u'ㅇ', u'ㅛ', u'')
        >>> print hangulize.hangul.join(_)
        요

    """
    pass


def complete_syllables(phonemes):
    """Separates each syllables and completes every syllable."""
    pass


def split_phonemes(word):
    """Returns the splitted phonemes from the word.

        >>> split_phonemes(u'안녕') #doctest: +NORMALIZE_WHITESPACE
        (<Choseong 'ㅇ'>, <Jungseong 'ㅏ'>, <Jongseong 'ㄴ'>,
         <Choseong 'ㄴ'>, <Jungseong 'ㅕ'>, <Jongseong 'ㅇ'>)
    """
    pass


def join_phonemes(phonemes):
    """Returns the word from the splitted phonemes::

        >>> print join_phonemes((Jungseong(A), Jongseong(N),
        ...                      Choseong(N), Jungseong(YEO), Jongseong(NG)))
        안녕

    """
    pass
