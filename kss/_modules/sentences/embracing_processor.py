# Copyright (C) 2021 Hyunwoong Ko <kevin.brain@kakaobrain.com> and Sang Park <sang.park@dnotitia.com>
# All rights reserved.


from functools import lru_cache
from itertools import chain
from typing import List, Dict, Tuple, Iterable, Optional

from kss._elements.subclasses import Syllable
from kss._utils.const import (
    double_quotes,
    double_quotes_open_to_close,
    double_quotes_close_to_open,
    single_quotes,
    single_quotes_open_to_close,
    single_quotes_close_to_open,
    single_quotes_wo_direction,
    double_quotes_wo_direction,
)


class EmbracingProcessor:
    def __init__(self):
        self.single_stack, self.double_stack = [], []
        self.single_pop, self.double_pop = "'", '"'
        self.single_idx, self.double_idx = 0, 0
        self.single_sent_idx, self.double_sent_idx = 0, 0

    def empty(self) -> bool:
        """
        Check all stacks are empty or not.

        Returns:
            bool: True if all stacks are empty else False.
        """
        pass

    def process(self, idx: int, sent_idx: int, syllable: Syllable):
        """
        Push or pop symbols to detect embraced sentences

        Args:
            idx (int): current syllable index
            sent_idx (int): current sentence index
            syllable (Syllable): current syllable object
        """
        pass

    def update_index(self, idx: int, sent_idx: int, syllable: Syllable):
        """
        Update indices of syllables and sentences

        Args:
            idx (int): current syllable index
            sent_idx (int): current sentence index
            syllable (Syllable): current syllable object
        """
        pass

    def realign(
        self,
        input_sentences: List[Syllable],
        output_sentences: List[List[Syllable]],
        func: "function",
    ) -> List[List[Syllable]]:
        """
        Realign wrongly split sentences because of all symbols.

        Args:
            input_sentences (List[Syllable]): input sentences
            output_sentences (List[List[Syllables]): split sentences from `_split_sentences`
            func (function): split function

        Returns:
            List[List[Syllable]]: corrected split sentences.
        """
        pass

    def _pop_symbol(
        self,
        syllable: Syllable,
        stack: List[str],
        open_to_close: Dict[str, str],
        close_to_open: Dict[str, str],
    ) -> str:
        """
        Pop symbols from given stack if the symbols are contained in given dictionaries.

        Args:
            syllable (Syllable): syllable object
            stack (List[str]): symbol stack
            open_to_close (Dict[str, str]): open to close dict
            close_to_open (Dict[str, str]): close to open dict

        Returns:
            str: popped symbol
        """
        pass

    def _realign_sentences(
        self,
        input_sentences: List[Syllable],
        output_sentences: List[List[Syllable]],
        idx: int,
        sent_idx: int,
        func: "function",
    ) -> List[List[Syllable]]:
        """
        Realign wrongly split sentences because of specific symbol.

        Args:
            input_sentences (List[Syllable]): input sentences
            output_sentences (List[List[Syllables]): split sentences from `_split_sentences`
            idx (int): current syllable index
            sent_idx (int): current sentence index
            func (function): split function

        Returns:
            List[List[Syllable]]: corrected split sentences.
        """
        pass

    @lru_cache(maxsize=500)
    def _realign_sub_sentences(
        self,
        output_sentences: Tuple,
        syllable: Syllable,
        idx_in_sent: int,
        func: "function",
    ):
        """
        Realign wrongly split sub-sentences because of specific symbol.

        Args:
            output_sentences (Tuple): tuple of syllables
            syllable (Syllable): problematic syllable
            idx_in_sent (int): syllable index in sentence
            func (function): split function

        Returns:
            List[List[Syllable]]: corrected split sub-sentences.
        """
        pass

    @staticmethod
    def get_idx_in_sent(
        output_sentences: List[List[Syllable]],
        idx: int,
        sent_idx: int,
    ) -> int:
        """
        Get syllable index in the sentence.

        Args:
            output_sentences (List[List[Syllables]): split sentences from `_split_sentences`
            idx (int): current syllable index
            sent_idx (int): current sentence index

        Returns:
            int: syllable index in sentence
        """
        pass

    @staticmethod
    def _top(stack: List[str], symbol: str) -> bool:
        """
        Is the symbol was top of the stack or not.

        Args:
            stack (List[str]): stack of symbols
            symbol (symbol): symbol string

        Returns:
            bool: whether the symbol was top of the stack or not.
        """
        pass

    def _empty(self, obj: Iterable, dim: int = 1) -> bool:
        """
        Check the length of object is 0.

        Args:
            obj (Iterable): iterable object
            dim (int): object dimension

        Returns:
            bool: whether the length of object is 0 or not.
        """
        pass

    def _push_pop_symbol(
        self,
        stack: List[str],
        symbol: str,
        current_char: str,
    ) -> Optional[str]:
        """
        Push or pop symbol in the list.

        Args:
            stack (List[str]): stack of symbols
            symbol (str): symbol string
            current_char (str): current character of the syllable

        Returns:
            Optional[str]: popped symbol string if the symbol was top, else returns None.
        """
        pass
