# Copyright (C) 2021 Hyunwoong Ko <kevin.brain@kakaobrain.com> and Sang Park <sang.park@dnotitia.com>
# All rights reserved.

# This code was copied from g2pk [https://github.com/kyubyong/g2pK]
# And modified by Hyunwoong Ko [https://github.com/hyunwoongko]

import re

# This is a list of bound nouns preceded by pure Korean numerals.
BOUND_NOUNS = "군데 권 개 그루 닢 대 두 마리 모 모금 뭇 발 발짝 방 번 벌 보루 살 수 술 시 쌈 움큼 정 짝 채 척 첩 축 켤레 톨 통"


def process_num(num, sino=True):
    """Process a string looking like arabic number.
    num: string. Consists of [0-9,]. e.g., 12,345
    sino: boolean. If True, sino-Korean numerals, i.e., 일, 이, .. are considered.
        Otherwise, pure Korean ones in their modifying forms such as 한, 두, ... are returned.

    >>> process_num("123,456,789", sino=True)
    일억이천삼백사십오만육천칠백팔십구

    >>> process_num("123,456,789", sino=False)
    일억이천삼백사십오만육천칠백여든아홉
    """
    pass


def convert_num(string):
    """Convert a annotated string such that arabic numerals inside are spelled out.
    >>> convert_num("우리 3시/B 10분/B에 만나자.")
    우리 세시/B 십분/B에 만나자.
    """
    pass
