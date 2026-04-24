# Copyright (C) 2021 Hyunwoong Ko <kevin.brain@kakaobrain.com> and Sang Park <sang.park@dnotitia.com>
# All rights reserved.

# This code is copied from soynlp [https://github.com/lovit/soynlp]
# And modified by Hyunwoong Ko [https://github.com/hyuwoongko]

import re
import sys
from functools import partial
from typing import Union, Tuple, Dict, Any, List

from kss._modules.preprocessing.completed_form import _incompleted_form_ratio
from kss._utils.multiprocessing import _run_job
from kss._utils.sanity_checks import _check_type, _check_num_workers, _check_text

hangul_pattern = re.compile(r'[ㄱ-ㅎㅏ-ㅣ가-힣]')
symbols_pattern = re.compile("#+")
punctuations = {'.', '!', '?', '。'}
parenthesis = {'(', ')', '[', ']', '{', '}', '<', '>'}
ellipsis_marks = {"...", "[...]", "(...)", "…", "[…]"}


def _get_ngrams(input_list, n):
    # Fast function to return n-grams from a list of tokens.
    pass


def _repeating_top_ngram_score(text, n):
    pass


def _repeating_duplicated_ngrams_score(text, n):
    pass


def _num_line_by_repeats(text, split_delimiter='\n'):
    pass


def _num_line_by_char_repeats(text, split_delimiter='\n'):
    pass


def _lines_started_with_bullets_ratio(text):
    pass


def _lines_ends_with_ellipsis_ratio(text):
    pass


def _symbols_to_word_ratio(text):
    pass


def filter_out(
    text: Union[str, List[str], Tuple[str]],
    min_length: int = 0,
    max_length: int = sys.maxsize,
    min_mean_words_length: int = 0,
    max_mean_words_length: int = sys.maxsize,
    min_words: int = 0,
    max_words: int = sys.maxsize,
    min_lines: int = 0,
    max_lines: int = sys.maxsize,
    min_paragraphs: int = 0,
    max_paragraphs: int = sys.maxsize,
    min_alphabet_ratio: float = 0,
    max_alphabet_ratio: float = 1,
    min_alphanumeric_ratio: float = 0,
    max_alphanumeric_ratio: float = 1,
    min_number_ratio: float = 0,
    max_number_ratio: float = 1,
    min_punctuation_ratio: float = 0,
    max_punctuation_ratio: float = 1,
    min_symbols_to_words_ratio: float = 0,
    max_symbols_to_words_ratio: float = 1,
    min_lines_started_with_bullets_ratio: float = 0,
    max_lines_started_with_bullets_ratio: float = 1,
    min_whitespace_ratio: float = 0,
    max_whitespace_ratio: float = 1,
    min_parenthesis_ratio: float = 0,
    max_parenthesis_ratio: float = 1,
    min_ellipsis_ratio: float = 0,
    max_ellipsis_ratio: float = 1,
    min_hangul_ratio: float = 0,
    max_hangul_ratio: float = 1,
    max_words_length: int = sys.maxsize,
    max_line_repeats: int = sys.maxsize,
    max_line_by_char_repeats: int = sys.maxsize,
    max_paragraph_repeats: int = sys.maxsize,
    max_paragraph_by_char_repeats: int = sys.maxsize,
    max_repeating_top_ngram_repeats_score: float = sys.maxsize,
    max_repeating_duplicate_ngrams_score: float = sys.maxsize,
    ngram_size_for_repeating_top_ngram_repeats: int = 3,
    ngram_size_for_repeating_duplicate_ngrams: int = 3,
    max_hangul_incompleted_form_ratio: float = 1,
    num_workers: Union[int, str] = "auto",
) -> Union[Tuple[bool, Dict[str, Any]], List[Tuple[bool, Dict[str, Any]]]]:
    """
    This filters out bad text based on various conditions.

    Args:
        text (Union[str, List[str], Tuple[str]]): single text or list of texts
        min_length (int): minimum length of text
        max_length (int): maximum length of text
        min_mean_words_length (int): minimum mean words length
        max_mean_words_length (int): maximum mean words length
        min_words (int): minimum number of words
        max_words (int): maximum number of words
        min_lines (int): minimum number of lines
        max_lines (int): maximum number of lines
        min_paragraphs (int): minimum number of paragraphs
        max_paragraphs (int): maximum number of paragraphs
        min_alphabet_ratio (float): minimum alphabet ratio
        max_alphabet_ratio (float): maximum alphabet ratio
        min_alphanumeric_ratio (float): minimum alphanumeric ratio
        max_alphanumeric_ratio (float): maximum alphanumeric ratio
        min_number_ratio (float): minimum number ratio
        max_number_ratio (float): maximum number ratio
        min_punctuation_ratio (float): minimum punctuation ratio
        max_punctuation_ratio (float): maximum punctuation ratio
        min_symbols_to_words_ratio (float): minimum symbols to words ratio
        max_symbols_to_words_ratio (float): maximum symbols to words ratio
        min_lines_started_with_bullets_ratio (float): minimum lines started with bullets ratio
        max_lines_started_with_bullets_ratio (float): maximum lines started with bullets ratio
        min_whitespace_ratio (float): minimum whitespace ratio
        max_whitespace_ratio (float): maximum whitespace ratio
        min_parenthesis_ratio (float): minimum parenthesis ratio
        max_parenthesis_ratio (float): maximum parenthesis ratio
        min_ellipsis_ratio (float): minimum ellipsis ratio
        max_ellipsis_ratio (float): maximum ellipsis ratio
        min_hangul_ratio (float): minimum hangul ratio
        max_hangul_ratio (float): maximum hangul ratio
        max_words_length (int): maximum words length
        max_line_repeats (int): maximum line repeats
        max_line_by_char_repeats (int): maximum line by char repeats
        max_paragraph_repeats (int): maximum paragraph repeats
        max_paragraph_by_char_repeats (int): maximum paragraph by char repeats
        max_repeating_top_ngram_repeats_score (float): maximum repeating top ngram repeats score
        max_repeating_duplicate_ngrams_score (float): maximum repeating duplicate ngrams score
        ngram_size_for_repeating_top_ngram_repeats (int): ngram size for repeating top ngram repeats
        ngram_size_for_repeating_duplicate_ngrams (int): ngram size for repeating duplicate ngrams
        max_hangul_incompleted_form_ratio (float): maximum hangul non completed form ratio
        num_workers (Union[int, str]): the number of multiprocessing workers

    Returns:
        Union[Tuple[bool, Dict[str, Any]], List[Tuple[bool, Dict[str, Any]]]]: filtered out text or list of filtered out texts

    Examples:
        >>> from kss import Kss
        >>> filter_out = Kss("filter_out")
        >>> text = "▲ 12월 17일 (목)=============================================================================시간 경기내용 방송사=============================================================================[축구] 프랑스 리그 103:00 (AS모나코-스타드 렌) SBS스포츠[축구] 09-10 UEFA 유로파리그04:00 (스파르타프라하-FC코펜하겐) MBC-ESPN[축구] 09-10 프리미어리그05:00 (토트넘-맨체스터시티) SBS스포츠-----------------------------------------------------------------------------[농구] 2009-10 NBA10:00 (LA레이커스-밀워키) SBS스포츠[농구] 2009-10 신한은행 여자농구17:00 (삼성생명-금호생명) SBS스포츠[농구] 2009-10 KCC 프로농구19:00 (KCC-KT) MBC-ESPN19:00 (LG-SK) SBS스포츠-----------------------------------------------------------------------------[배구] 2009-10 NH농협 V리그17:00 (흥국생명-현대건설)19:00 (대한항공-신협상무) KBS N 스포츠-----------------------------------------------------------------------------19:20 [핸드볼] 2009 세계여자선수권대회-----------------------------------------------------------------------------19:00 [배드민턴] 한국 최강전=============================================================================※ 상기 경기일정 및 방송 편성정보는 사정에 따라 변동될 수 있습니다< pre >/한국아이닷컴 뉴스부 한국아이닷컴 뉴스부 '스타화보 VM' 무료다운받기 [**8253+NATE 또는 통화] [ⓒ 인터넷한국일보(www.hankooki.com), 무단 전재 및 재배포 금지]"
        >>> output = filter_out(text, min_mean_words_length=2, max_mean_words_length=10)
        >>> print(output)
        (True, {'reason': 'mean_words_length', 'value': 13.025316455696203})
    """
    pass


def _filter_out(
    text,
    min_length=0,
    max_length=sys.maxsize,
    min_mean_words_length=0,
    max_mean_words_length=sys.maxsize,
    min_words=0,
    max_words=sys.maxsize,
    min_lines=0,
    max_lines=sys.maxsize,
    min_paragraphs=0,
    max_paragraphs=sys.maxsize,
    min_alphabet_ratio=0,
    max_alphabet_ratio=1,
    min_alphanumeric_ratio=0,
    max_alphanumeric_ratio=1,
    min_number_ratio=0,
    max_number_ratio=1,
    min_punctuation_ratio=0,
    max_punctuation_ratio=1,
    min_symbols_to_words_ratio=0,
    max_symbols_to_words_ratio=1,
    min_lines_started_with_bullets_ratio=0,
    max_lines_started_with_bullets_ratio=1,
    min_whitespace_ratio=0,
    max_whitespace_ratio=1,
    min_parenthesis_ratio=0,
    max_parenthesis_ratio=1,
    min_ellipsis_ratio=0,
    max_ellipsis_ratio=1,
    min_hangul_ratio=0,
    max_hangul_ratio=1,
    max_words_length=sys.maxsize,
    max_line_repeats=sys.maxsize,
    max_line_by_char_repeats=sys.maxsize,
    max_paragraph_repeats=sys.maxsize,
    max_paragraph_by_char_repeats=sys.maxsize,
    max_repeating_top_ngram_repeats_score=sys.maxsize,
    max_repeating_duplicate_ngrams_score=sys.maxsize,
    ngram_size_for_repeating_top_ngram_repeats=3,
    ngram_size_for_repeating_duplicate_ngrams=3,
    max_hangul_incompleted_form_ratio=1,
):
    pass
