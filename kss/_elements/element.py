# Copyright (C) 2021 Hyunwoong Ko <kevin.brain@kakaobrain.com> and Sang-Kil Park <skpark1224@hyundai.com>
# All rights reserved.

from dataclasses import dataclass
from functools import lru_cache
from typing import Optional, Tuple, Union

from kss._elements.empty import Empty


@dataclass
class Element(object):
    _next: "Element" = None
    _prev: "Element" = None

    def __init__(self, text, pos, idx):
        self.text = text
        self.pos = pos
        self.idx = idx

    def __str__(self):
        return str((self.text, self.pos, self.idx))

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return other.text == self.text and other.pos == self.pos and other.idx == self.idx

    def __hash__(self):
        return hash((self.text, self.pos, self.idx))

    @property
    def next(self):
        if self._next is None:
            return Empty()
        return self._next

    @next.setter
    def next(self, _next):
        self._next = _next

    @property
    def prev(self):
        if self._prev is None:
            return Empty()
        return self._prev

    @prev.setter
    def prev(self, _prev):
        self._prev = _prev

    def next_skip(self, *poses, exclude=None):
        pass

    def prev_skip(self, *poses, exclude=None):
        pass

    def prev_skip_from_current(self, *poses, exclude=None):
        pass

    def next_skip_from_current(self, *poses, exclude=None):
        pass

    def check_pos(self, *poses, exclude: Optional[Tuple] = None) -> bool:
        """
        Check pos of given syllable.

        Args:
            poses (str): poses for check
            exclude (Optional[Tuple]): excluded poses

        Returns:
            bool: whether pos of the syllable is contained in input poses or not.
        """
        pass

    def check_text(self, *texts, exclude: Optional[Tuple] = None) -> bool:
        """
        Check text of given syllable.

        Args:
            texts (str): texts for check
            exclude (Optional[Tuple]): excluded texts

        Returns:
            bool: whether text of the syllable is contained in input texts or not.
        """
        pass

    def check_pos_and_text(
        self,
        poses: Union[str, Tuple],
        texts: Union[str, Tuple],
        exclude_poses: Optional[Tuple] = None,
        exclude_texts: Optional[Tuple] = None,
    ):
        """
        Check pos and text at the same time

        Args:
            poses: poses for check
            texts (Tuple): texts for check
            exclude_poses (Optional[Tuple]): excluded poses
            exclude_texts (Optional[Tuple]): excluded texts

        Returns:
            bool: whether pos and text of the syllable are contained in input poses and texts.
        """
        pass

    def check_texts(self, text: str) -> bool:
        """
        Check texts of current and next syllables

        Args:
            text (str): texts for check

        Returns:
            bool: whether text of the current and next syllables re contained in input text or not.
        """
        pass
