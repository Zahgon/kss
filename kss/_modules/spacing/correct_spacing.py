# Copyright (C) 2021 Hyunwoong Ko <kevin.brain@kakaobrain.com> and Sang Park <sang.park@dnotitia.com>
# All rights reserved.

# Core algorithm was copied from Kiwi (https://github.com/bab2min/kiwipiepy).
# And modified by Hyunwoong Ko [https://github.com/hyunwoongko]
import re
from functools import partial
from typing import Union, List, Tuple

from kss._elements.subclasses import Token
from kss._modules.morphemes.analyzers import Analyzer
from kss._modules.morphemes.split_morphemes import split_morphemes
from kss._modules.morphemes.utils import _reset_spaces
from kss._modules.sentences.split_sentences import _split_sentences
from kss._modules.spacing.utils import postprocess, postprocess_heuristic
from kss._utils.multiprocessing import _run_job
from kss._utils.sanity_checks import _check_text, _check_analyzer_backend_mecab_pecab_only, _check_num_workers

any_ws = re.compile(r"\s+")
space_insertable = r"(([^SUWX]|X[RS]|S[EH]).* ([NMI]|V[VAX]|VCN|XR|XPN|S[WLHN]))|(SN ([MI]|N[PR]|NN[GP]|V[VAX]|VCN|XR|XPN|S[WHN]))|((S[FPL]).* ([NMI]|V[VAX]|VCN|XR|XPN|S[WHN]))"
space_insertable = re.compile(space_insertable)

backup_dict = {
    "ㆍ": "/ㆍ/",
    "\n": "\u2424",  # Symbol for newline
    "\t": "\u2409",  # Symbol for horizontal tab
    "\r": "\u240D",  # Symbol for carriage return
    "\f": "\u240C",  # Symbol for form feed
    "\v": "\u240B",  # Symbol for vertical tab
}
restore_dict = {
    v: k for k, v in backup_dict.items()
}


def correct_spacing(
    text: Union[str, List[str], Tuple[str]],
    backend: str = "auto",
    num_workers: Union[int, str] = "auto",
    reset_whitespaces: bool = False,
    return_morphemes: bool = False,
) -> Union[str, List[str]]:
    """
    This corrects the spacing of the text.

    Args:
        text (Union[str, List[str], Tuple[str]]): single text or list/tuple of texts
        backend (str): morpheme analyzer backend. 'mecab', 'pecab' are supported
        num_workers (Union[int, str])): the number of multiprocessing workers
        reset_whitespaces (bool): reset whitespaces or not
        return_morphemes (bool): whether to return morphemes or not

    Returns:
        Union[str, List[str]]: corrected text or list of corrected texts

    Examples:
        >>> from kss import Kss
        >>> correct_spacing = Kss("correct_spacing")
        >>> text = "아버지가방에들어가시다"
        >>> correct_spacing(text)
        '아버지가 방에 들어가시다'

    References:
        This was copied from [Kiwi](https://github.com/bab2min/kiwipiepy) and [ko-prfrdr](https://github.com/ychoi-kr/ko-prfrdr)
        and modified by Kss
    """
    pass


def _correct_spacing(
    text: str,
    backend: Analyzer,
    backend_string: str,
    reset_whitespaces: bool = False,
    return_morphemes: bool = False,
) -> Union[str, Tuple[str, List[Tuple[str, str]]]]:
    pass
