# Copyright (C) 2021 Hyunwoong Ko <kevin.brain@kakaobrain.com> and Sang Park <sang.park@dnotitia.com>
# All rights reserved.


from functools import partial, lru_cache
from typing import List, Union, Tuple, Any

from kss._modules.morphemes.utils import _reset_spaces

from kss._elements.subclasses import Syllable
from kss._modules.morphemes.analyzers import Analyzer
from kss._modules.sentences.embracing_processor import EmbracingProcessor
from kss._modules.sentences.sentence_postprocessor import SentencePostprocessor
from kss._modules.sentences.sentence_preprocessor import SentencePreprocessor
from kss._modules.sentences.sentence_splitter import SentenceSplitter
from kss._utils.multiprocessing import _run_job
from kss._utils.sanity_checks import (
    _check_num_workers,
    _check_text,
    _check_analyzer_backend,
    _check_type,
    _check_iterable_type,
)

preprocessors = {(): SentencePreprocessor()}
postprocessors = {(): SentencePostprocessor()}


def split_sentences(
    text: Union[str, List[str], Tuple[str]],
    backend: str = "auto",
    num_workers: Union[int, str] = "auto",
    strip: bool = True,
    return_morphemes: bool = False,
    ignores: List[str] = None,
) -> Union[List[str], List[List[str]]]:
    """
    This splits texts into sentences.

    Args:
        text (Union[str, List[str], Tuple[str]]): single text or list/tuple of texts
        backend (str): morpheme analyzer backend. 'mecab', 'pecab', 'punct', 'fast' are supported
        num_workers (Union[int, str])): the number of multiprocessing workers
        strip (bool): strip all sentences or not
        return_morphemes (bool): whether to return morphemes or not
        ignores (List[str]): list of strings to ignore

    Returns:
        Union[List[str], List[List[str]]]: outputs of sentence splitting

    Examples:
        >>> from kss import Kss
        >>> split_sentences = Kss("split_sentences")
        >>> text = "회사 동료 분들과 다녀왔는데 분위기도 좋고 음식도 맛있었어요 다만, 강남 토끼정이 강남 쉑쉑버거 골목길로 쭉 올라가야 하는데 다들 쉑쉑버거의 유혹에 넘어갈 뻔 했답니다 강남역 맛집 토끼정의 외부 모습."
        >>> split_sentences(text)
        ['회사 동료 분들과 다녀왔는데 분위기도 좋고 음식도 맛있었어요', '다만, 강남 토끼정이 강남 쉑쉑버거 골목길로 쭉 올라가야 하는데 다들 쉑쉑버거의 유혹에 넘어갈 뻔 했답니다', '강남역 맛집 토끼정의 외부 모습.']
    """
    pass


@lru_cache(maxsize=500)
def _split_sentences(
    text: Union[str, Tuple[Syllable]],
    backend: Analyzer,
    strip: bool,
    postprocess: bool = True,
    recursion: int = 0,
    return_morphemes: bool = False,
    preprocessor: SentencePreprocessor = preprocessors[()],
    postprocessor: SentencePostprocessor = postprocessors[()],
):
    """
    Split texts into sentences.

    Args:
        text (Union[str, List[Syllable]]): single text
        backend (str): morpheme analyzer backend
        strip (bool): strip all sentences or not
        postprocess (bool): whether it uses postprocessing or not
        recursion (int): recursion times
        return_morphemes (bool): whether to return morphemes or not
        preprocessor (SentencePreprocessor): sentence preprocessor
        postprocessor (SentencePostprocessor): sentence postprocessor

    Returns:
        List[str]: outputs of sentence splitting.
    """
    pass
