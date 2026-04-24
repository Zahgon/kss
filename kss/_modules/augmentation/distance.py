# Copyright (C) 2021 Hyunwoong Ko <kevin.brain@kakaobrain.com> and Sang Park <sang.park@dnotitia.com>
# All rights reserved.

import jamo
import numpy as np

hangul_distance_map = {}
hangul_distance_map.update({lead: 0.5 for lead in jamo.JAMO_LEADS})
hangul_distance_map.update({vowel: 0.5 for vowel in jamo.JAMO_VOWELS})
hangul_distance_map.update({tail: 0.25 for tail in jamo.JAMO_TAILS})


def hangul_levenshtein(
    a,
    b,
    normalize=False,
    decompose=True,
    lowercase=False,
    verbose=False,
    insertions_cost_ratio=0.6,
    deletions_cost_ratio=0.4,
):
    """
    In most, Korean people can identify a word even if only the lead consonants of the word are given.
    For example, 'ㄱ' and 'ㅅ' can be identified as '감사' and 'ㅎ' and 'ㅇ' can be identified as '하이'.
    But, if only tail consonants of the word are given, it is very hard to identify the word.
    For example, We can't identify it's '감사' if ['ㅁ', None] is given.

    Let's say we have a source word and two candidate words like the following:

    - source_word = "또또칸"
    - candidate_1 = "똑똑한"
    - candidate_2 = "고소한"

    With original Levenshtein distance, the distance between `source_word` and `candidate_1` is 3
    and the distance between `source_word` and `candidate_2` is also 3. But, with Hangul Levenshtein
    distance, the distance between `source_word` and `candidate_1` can be decreased to 0.7, but the
    distance between `source_word` and `candidate_2` is 1.5. And we all know that '똑똑한' is much
    closer to '또또칸' than '고소한'.
    """
    pass
