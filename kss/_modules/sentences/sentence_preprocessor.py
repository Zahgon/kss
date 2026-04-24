# Copyright (C) 2021 Hyunwoong Ko <kevin.brain@kakaobrain.com> and Sang Park <sang.park@dnotitia.com>
# All rights reserved.


from typing import List, Tuple

from kss._elements.subclasses import Syllable
from kss._modules.sentences.sentence_processor import SentenceProcessor
from kss._utils.const import (
    bracket_open_to_close,
    bracket_close_to_open,
    quotes_open_to_close,
    quotes_close_to_open,
    special_symbols_for_split,
    jamo,
    spaces,
    special_symbols_for_suffix,
    daggers,
    circle_bracket_charaters,
)
from kss._utils.emojis import _emojis


class SentencePreprocessor(SentenceProcessor):

    _correction = {
        lambda c, p: c in circle_bracket_charaters: "SN",
        lambda c, p: c in special_symbols_for_split or c in daggers: "PF",  # Prefix
        lambda c, p: c in "!?.": "SF",
        lambda c, p: c in ",:/ㆍ": "SC",
        lambda c, p: c in "".join(bracket_open_to_close): "SSO",
        lambda c, p: c in "".join(bracket_close_to_open): "SSC",
        lambda c, p: c in "`'\"″": "QTN",  # quotes normal
        lambda c, p: c in "".join(quotes_open_to_close): "QTO",  # quotes open
        lambda c, p: c in "".join(quotes_close_to_open): "QTC",  # quotes close
        lambda c, p: c in jamo: "JAMO",
        lambda c, p: c == "요" and ("EC" in p or "JX" == p): "EF",
        lambda c, p: (
            c == "^" or c in _emojis or c in special_symbols_for_suffix
        ): "EMOJI",
        lambda c, p: c in spaces: "SP",
    }

    def preprocess(self, input_morphemes: List[Tuple[str, str]]) -> List[Syllable]:
        """
        Convert mecab morphemes to syllables and correct wrong tags

        Args:
            input_morphemes (List[Tuple[str, str]]): input morphemes

        Returns:
            List[Syllable]: syllables in input text
        """
        pass

    def _convert_morphemes_to_syllables(
        self, input_morphemes: List[Tuple[str, str]]
    ) -> List[Syllable]:
        """
        Convert mecab morphemes to syllables.

        Args:
            input_morphemes (List[Tuple[str, str]]): input morphemes

        Returns:
            List[Syllable]: syllables in input text.
        """
        pass

    def _correct_wrong_tags(self, syllables: List[Syllable]):
        """
        Convert mecab morphemes to syllables and preprocess syllables

        Args:
            syllables (List[Syllable]): input syllables

        Returns:
            List[Syllable]: syllables in input text
        """
        pass

    @staticmethod
    def _change_poses(syllable: Syllable, *poses: str):
        """
        Change poses from the given syllable.
        This method could make a huge problem, so this implemented in preprocessor class.

        Args:
            syllable (Syllable): input syllable
            *poses (str): poses to be changed
        """
        pass

    @staticmethod
    def _append_space_before_emoji(syllables: List[Syllable]) -> List[Syllable]:
        """
        Append a space character before emoji character.
        This could be helpful for tokenizing sentences which contain emoji.

        Args:
            syllables (List[Syllable]): input syllables

        Returns:
            List[Syllable]: preprocessed syllables
        """
        pass
