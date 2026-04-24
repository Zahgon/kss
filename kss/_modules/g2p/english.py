# Copyright (C) 2021 Hyunwoong Ko <kevin.brain@kakaobrain.com> and Sang Park <sang.park@dnotitia.com>
# All rights reserved.

# This code was copied from g2pk [https://github.com/kyubyong/g2pK]
# And modified by Hyunwoong Ko [https://github.com/hyunwoongko]


import re

from kss._modules.g2p.utils import adjust, to_choseong, to_jungseong, to_jongseong, reconstruct, cmu
from kss._modules.jamo._jamo import j2h


def convert_eng(string):
    """Convert a string such that English words inside are turned into Hangul.
    string: input string.
    cmu: cmu dict object.

    >>> convert_eng("그 사람 좀 old school이야", cmu)
    그 사람 좀 올드 스쿨이야
    """
    pass
