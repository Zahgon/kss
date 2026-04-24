# Copyright (C) 2021 Hyunwoong Ko <kevin.brain@kakaobrain.com> and Sang Park <sang.park@dnotitia.com>
# All rights reserved.


import re
from functools import lru_cache
from typing import List

from kss._utils.const import (
    alphabet_with_quotes,
    url_pattern,
    email_pattern,
    backup_normal,
)


class SentenceProcessor:
    _all_s_exclude = ("QTO",)
    _all_s_poses = ("SP", "SF", "SY", "SE", "SSC", "QTC", "QTN", "EMOJI", "JAMO")
    _all_s_poses_wo_qtn = ("SP", "SF", "SY", "SE", "SSC", "QTC", "EMOJI", "JAMO")

    _heavy_backup = {}
    _heavy_backup.update(
        {
            k: {_v: str(abs(hash(_v))) for _v in v}
            for k, v in alphabet_with_quotes.items()
        }
    )
    _normal_backup = {k: str(abs(hash(k))) for k in sorted(backup_normal)}

    def __init__(self, ignores: List[str] = None):
        self.ignores = ignores
        if self.ignores is not None:
            self._normal_backup.update({k: str(abs(hash(k))) for k in self.ignores})

    @staticmethod
    def _replace(text: str, purpose_dict: dict, restore: bool = False):
        pass

    def _add_url_or_email(self, text):
        pass

    @lru_cache(100)
    def backup(self, inputs: str):
        pass

    @lru_cache(100)
    def restore(self, outputs: str, inputs: str):
        pass
