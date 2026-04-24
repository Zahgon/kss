# -*- coding: utf-8 -*-
"""
    hangulize.normalization
    ~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2010-2017 by Heungsub Lee
    :license: BSD, see LICENSE for more details.
"""
import unicodedata


__all__ = ['normalize_roman']


def normalize_roman(string, additional=None):
    """Removes diacritics from the string and converts to lowercase::

        >>> normalize_roman(u'Eèé')
        u'eee'

    """
    def gen():
        pass

    pass
