# Copyright (C) 2021 Hyunwoong Ko <kevin.brain@kakaobrain.com> and Sang Park <sang.park@dnotitia.com>
# All rights reserved.

import sys
from functools import partial
from typing import List, Optional, Tuple, Union

from kss._modules.preprocessing.anonymize import _anonymize
from kss._modules.preprocessing.filter_out import _filter_out
from kss._modules.preprocessing.normalize import _normalize
from kss._utils.multiprocessing import _run_job
from kss._utils.sanity_checks import _check_text, _check_type, _check_num_workers


def preprocess(
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
    max_symbols_to_words_ratio: float = 0,
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
    max_hangul_incompleted_form_ratio: float = 1,
    max_words_length: int = sys.maxsize,
    max_line_repeats: int = sys.maxsize,
    max_line_by_char_repeats: int = sys.maxsize,
    max_paragraph_repeats: int = sys.maxsize,
    max_paragraph_by_char_repeats: int = sys.maxsize,
    max_repeating_top_ngram_repeats_score: float = sys.maxsize,
    max_repeating_duplicate_ngrams_score: float = sys.maxsize,
    ngram_size_for_repeating_top_ngram_repeats: int = 3,
    ngram_size_for_repeating_duplicate_ngrams: int = 3,
    phone_number_anonymization: bool = True,
    rrn_anonymization: bool = True,
    card_anonymization: bool = True,
    email_anonymization: bool = True,
    bank_account_anonymization: bool = True,
    credit_card_anonymization: bool = True,
    zip_anonymization: bool = True,
    bitcoin_anonymization: bool = True,
    url_anonymization: bool = True,
    ip_v6_anonymization: bool = True,
    ip_v4_anonymization: bool = True,
    phone_number_replacement: str = "<PHONE_NUMBER>",
    rrn_replacement: str = "<RRN>",
    card_replacement: str = "<CARD>",
    email_replacement: str = "<EMAIL>",
    bank_account_replacement: str = "<BANK_ACCOUNT>",
    credit_card_replacement: str = "<CREDIT_CARD>",
    zip_replacement: str = "<ZIP>",
    bitcoin_replacement: str = "<BITCOIN>",
    url_replacement: str = "<URL>",
    ip_v6_replacement: str = "<IPV6>",
    ip_v4_replacement: str = "<IPV4>",
    num_workers: Union[int, str] = "auto",
) -> Union[str, List[str]]:
    """
    This preprocesses text with various options.
    This does 1) normalization, 2) filtering out, and 3) anonymization in order.

    Args:
        text (Union[str, List[str], Tuple[str]]): single text or list of texts
        normalization_type (Optional[str]): normalization type
        allow_doubled_spaces (bool): whether to allow doubled spaces or not
        allow_html_tags (bool): whether to allow HTML tags or not
        allow_html_escape (bool): whether to allow HTML escape or not
        allow_halfwidth_hangul (bool): whether to allow halfwidth Hangul or not
        allow_hangul_jamo (bool): whether to allow Hangul jamo or not
        allow_invisible_chars (bool): whether to allow invisible characters or not
        reduce_char_repeats_over (int): the maximum number of character that can be repeated
        reduce_emoticon_repeats_over (int): the maximum number of emoticon that can be repeated
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
        min_hangul_ratio (float): minimum Hangul ratio
        max_hangul_ratio (float): maximum Hangul ratio
        max_hangul_incompleted_form_ratio (float): maximum Hangul non-completed form ratio
        max_words_length (int): maximum words length
        max_line_repeats (int): maximum line repeats
        max_line_by_char_repeats (int): maximum line by char repeats
        max_paragraph_repeats (int): maximum paragraph repeats
        max_paragraph_by_char_repeats (int): maximum paragraph by char repeats
        max_repeating_top_ngram_repeats_score (float): maximum repeating top ngram repeats score
        max_repeating_duplicate_ngrams_score (float): maximum repeating duplicate ngrams score
        ngram_size_for_repeating_top_ngram_repeats (int): ngram size for repeating top ngram repeats
        ngram_size_for_repeating_duplicate_ngrams (int): ngram size for repeating duplicate ngrams
        phone_number_anonymization (bool): whether to anonymize phone number or not
        rrn_anonymization (bool): whether to anonymize RRN or not
        card_anonymization (bool): whether to anonymize card or not
        email_anonymization (bool): whether to anonymize email or not
        bank_account_anonymization (bool): whether to anonymize bank account or not
        credit_card_anonymization (bool): whether to anonymize credit card or not
        zip_anonymization (bool): whether to anonymize zip or not
        bitcoin_anonymization (bool): whether to anonymize bitcoin or not
        url_anonymization (bool): whether to anonymize URL or not
        ip_v6_anonymization (bool): whether to anonymize IPv6 or not
        ip_v4_anonymization (bool): whether to anonymize IPv4 or not
        phone_number_replacement (str): replacement for phone number
        rrn_replacement (str): replacement for RRN
        card_replacement (str): replacement for card
        email_replacement (str): replacement for email
        bank_account_replacement (str): replacement for bank account
        credit_card_replacement (str): replacement for credit card
        zip_replacement (str): replacement for zip
        bitcoin_replacement (str): replacement for bitcoin
        url_replacement (str): replacement for URL
        ip_v6_replacement (str): replacement for IPv6
        ip_v4_replacement (str): replacement for IPv4
        num_workers (Union[int, str]): the number of multiprocessing workers

    Returns:
        Union[Tuple[str, Dict[str, Any]], List[Tuple[str, Dict[str, Any]]]]:
            preprocessed text and filtering metadata or list of preprocessed texts and filtering metadata
    """
    pass


def _preprocess(
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
    max_symbols_to_words_ratio=0,
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
    max_hangul_incompleted_form_ratio=1,
    max_words_length=sys.maxsize,
    max_line_repeats=sys.maxsize,
    max_line_by_char_repeats=sys.maxsize,
    max_paragraph_repeats=sys.maxsize,
    max_paragraph_by_char_repeats=sys.maxsize,
    max_repeating_top_ngram_repeats_score=sys.maxsize,
    max_repeating_duplicate_ngrams_score=sys.maxsize,
    ngram_size_for_repeating_top_ngram_repeats=3,
    ngram_size_for_repeating_duplicate_ngrams=3,
    phone_number_anonymization=True,
    rrn_anonymization=True,
    card_anonymization=True,
    email_anonymization=True,
    bank_account_anonymization=True,
    credit_card_anonymization=True,
    zip_anonymization=True,
    bitcoin_anonymization=True,
    url_anonymization=True,
    ip_v6_anonymization=True,
    ip_v4_anonymization=True,
    phone_number_replacement="<PHONE_NUMBER>",
    rrn_replacement="<RRN>",
    card_replacement="<CARD>",
    email_replacement="<EMAIL>",
    bank_account_replacement="<BANK_ACCOUNT>",
    credit_card_replacement="<CREDIT_CARD>",
    zip_replacement="<ZIP>",
    bitcoin_replacement="<BITCOIN>",
    url_replacement="<URL>",
    ip_v6_replacement="<IPV6>",
    ip_v4_replacement="<IPV4>",
):
    # 1. normalize text
    pass
