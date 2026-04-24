# Copyright (C) 2021 Hyunwoong Ko <kevin.brain@kakaobrain.com> and Sang Park <sang.park@dnotitia.com>
# All rights reserved.

# This was copied from KoEDA [https://github.com/toriving/KoEDA]
# And modified by Hyunwoong Ko [https://github.com/hyunwoongko]

import json
import os

from kss._modules.morphemes.split_morphemes import split_morphemes
from kss._modules.josa.josa import select_josa

WORDNET_JSON_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "assets/wordnet.json"
)

with open(WORDNET_JSON_PATH, "r", encoding="utf-8") as f:
    WORDNET = json.load(f)


def get_synonyms(word, min_length=None):
    pass


def correct_josa(text: str):
    pass
