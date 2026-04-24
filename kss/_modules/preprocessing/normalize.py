# Copyright (C) 2021 Hyunwoong Ko <kevin.brain@kakaobrain.com> and Sang Park <sang.park@dnotitia.com>
# All rights reserved.

import html
import re
import sys
import unicodedata
from functools import partial
from typing import Union, List, Optional, Tuple

from bs4 import BeautifulSoup

from kss._modules.jamo.utils import _j2h
from kss._modules.preprocessing.half2full import _half2full
from kss._modules.preprocessing.reduce_repeats import _reduce_char_repeats, _reduce_emoticon_repeats
from kss._modules.preprocessing.remove_invisible_chars import _remove_invisible_chars
from kss._utils.multiprocessing import _run_job
from kss._utils.sanity_checks import _check_text, _check_type, _check_num_workers

doubled_spaces_pattern = re.compile('(\s)\\1{2,}')


def normalize(
    text: Union[str, List[str], Tuple[str]],
    normalization_type: Optional[str] = None,
    allow_doubled_spaces: bool = True,
    allow_html_tags: bool = True,
    allow_html_escape: bool = True,
    allow_halfwidth_hangul: bool = True,
    allow_hangul_jamo: bool = True,
    allow_invisible_chars: bool = True,
    reduce_char_repeats_over: int = sys.maxsize,
    reduce_emoticon_repeats_over: int = sys.maxsize,
    num_workers: Union[int, str] = "auto",
) -> Union[str, List[str]]:
    """
    This normalizes text with various options.

    Args:
        text (Union[str, List[str], Tuple[str]]): single text or list of texts
        normalization_type (Optional[str]): normalization type
        allow_doubled_spaces (bool): whether to allow doubled spaces or not
        allow_html_tags (bool): whether to allow HTML tags or not
        allow_html_escape (bool): whether to allow HTML unescape or not
        allow_halfwidth_hangul (bool): whether to allow halfwidth Hangul or not
        allow_hangul_jamo (bool): whether to allow Hangul jamo or not
        allow_invisible_chars (bool): whether to allow invisible characters or not
        reduce_char_repeats_over (int): the maximum number of character that can be repeated
        reduce_emoticon_repeats_over (int): the maximum number of emoticon that can be repeated
        num_workers (Union[int, str]): the number of multiprocessing workers

    Returns:
        Union[str, List[str]]: normalized text or list of normalized texts

    Examples:
        >>> from kss import Kss
        >>> normalize = Kss("normalize")
        >>> text = "안녕\u200b하세요 ﾻﾻﾻﾻﾻﾻ   <br>오늘\u200b은 날이 참 좋네요.\\n\\n\\n200 &lt; 300 &amp; 400"
        >>> normalize(text, allow_doubled_spaces=False, allow_html_tags=False, allow_html_escape=False, allow_halfwidth_hangul=False, allow_hangul_jamo=False, allow_invisible_chars=False, reduce_char_repeats_over=2, reduce_emoticon_repeats_over=2)
        '안녕하세요 ㅋㅋ 오늘은 날이 참 좋네요.\\n200 < 300 & 400'
    """
    pass


def _normalize(
    text,
    normalization_type=None,
    allow_doubled_spaces=True,
    allow_html_tags=True,
    allow_html_escape=True,
    allow_halfwidth_hangul=True,
    allow_hangul_jamo=True,
    allow_invisible_chars=True,
    reduce_char_repeats_over=sys.maxsize,
    reduce_emoticon_repeats_over=sys.maxsize,
):
    pass
