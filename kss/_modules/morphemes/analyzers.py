# Copyright (C) 2021 Hyunwoong Ko <kevin.brain@kakaobrain.com> and Sang Park <sang.park@dnotitia.com>
# All rights reserved.

from abc import ABC
from functools import lru_cache
from typing import Tuple, List, Any

from kss._modules.morphemes.utils import _get_mecab, _get_pecab, _preserve_space
from kss._utils.const import spaces


class Analyzer(ABC):
    _analyzer, _backend = None, None

    def pos(self, text: str, drop_space: bool) -> Any:
        pass

    @staticmethod
    def _drop_space(tokens: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
        pass


class MecabAnalyzer(Analyzer):
    # `_analyzer` object must be class variable because of multiprocessing
    try:
        _analyzer, _backend = _get_mecab()
    except Exception:
        _analyzer, _backend = None, None

    @lru_cache(maxsize=500)
    def pos(self, text: str, drop_space: bool) -> List[Tuple[str, str]]:
        """
        Get pos information.

        Args:
            text (str): input text
            drop_space (bool): drop all spaces or not.

        Returns:
            List[Tuple[str, str]]: output of analysis.
        """
        pass


class PecabAnalyzer(Analyzer):
    # `_analyzer` object must be class variable because of multiprocessing
    try:
        _analyzer, _backend = _get_pecab()
    except Exception:
        _analyzer, _backend = None, None

    @lru_cache(maxsize=500)
    def pos(self, text: str, drop_space: bool) -> List[Tuple[str, str]]:
        """
        Get pos information.

        Args:
            text (str): input text
            drop_space (bool): drop all spaces or not.

        Returns:
            List[Tuple[str, str]]: output of analysis.
        """
        pass


class CharacterAnalyzer(Analyzer):
    _analyzer, _backend = None, "character"

    @lru_cache(maxsize=500)
    def pos(self, text: str, drop_space: bool) -> List[Tuple[str, str]]:
        """
        Get pos information.

        Args:
            text (str): input text
            drop_space (bool): drop all spaces or not.

        Returns:
            List[Tuple[str, str]]: output of analysis.
        """
        pass


class FastAnalyzer(CharacterAnalyzer):
    _analyzer, _backend = None, "fast"
