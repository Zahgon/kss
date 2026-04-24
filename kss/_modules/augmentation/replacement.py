# Copyright (C) 2021 Hyunwoong Ko <kevin.brain@kakaobrain.com> and Sang Park <sang.park@dnotitia.com>
# All rights reserved.

# This was copied from KoEDA [https://github.com/toriving/KoEDA]
# And modified by Hyunwoong Ko [https://github.com/hyunwoongko]

import random
from itertools import repeat, chain
from typing import Union, List

from kss._modules.morphemes.split_morphemes import split_morphemes
from kss._modules.augmentation.utils import get_synonyms
from kss._modules.augmentation.distance import hangul_levenshtein


class SynonymReplacement:
    def __init__(self, backend):
        self.backend = backend

    def __call__(self, *args, **kwargs):
        return self.synonym_replacement(*args, **kwargs)

    def synonym_replacement(
        self, data: Union[List[str], str], p: float = 0.1, repetition: int = 1, verbose: bool = False
    ) -> Union[List[str], str]:
        pass

    def _replacement(self, data: str, p: float = 0.1, verbose: bool=False) -> str:
        pass
