# Copyright (C) 2021 Hyunwoong Ko <kevin.brain@kakaobrain.com> and Sang Park <sang.park@dnotitia.com>
# All rights reserved.

# This code was copied from KR-WordRank [https://github.com/lovit/KR-WordRank]
# And modified by Hyunwoong Ko [https://github.com/hyuwoongko]

# Almost all code for wordrank is same with the original code.
# But there are unnecessary dependencies (scikit-learn, numpy, scipy).
# So I removed such dependencies for this project.

from collections import defaultdict

from kss._modules.morphemes.split_morphemes import split_morphemes


def hits(graph, beta, max_iter=50, bias=None, verbose=True,
         sum_weight=100, number_of_nodes=None, converge=0.001):
    """
    It trains rank of node using HITS algorithm.

    Arguments
    ---------
    graph : dict of dict
        Adjacent subword graph. graph[int][int] = float
    beta : float
        PageRank damping factor
    max_iter : int
        Maximum number of iterations
    bias : None or dict
        Bias vector
    verbose : Boolean
        If True, it shows training progress.
    sum_weight : float
        Sum of weights of all nodes in graph
    number_of_nodes : None or int
        Number of nodes in graph
    converge : float
        Minimum rank difference between previous step and current step.
        If the difference is smaller than converge, it do early-stop.

    Returns
    -------
    rank : dict
        Rank dictionary formed as {int:float}.
    """
    pass


def _update(rank, graph, bias, dw, beta):
    pass


def summarize_with_keywords(texts, num_keywords=100, stopwords=None, min_count=5,
                            max_length=10, beta=0.85, max_iter=10, num_rset=-1, verbose=False):
    """
    It train KR-WordRank to extract keywords from texts.

        >>> from krwordrank.word import summarize_with_keywords

        >>> texts = [] # list of str
        >>> keywords = summarize_with_keywords(texts, num_keywords=100, min_count=5)

    Arguments
    ---------
    texts : list of str
        Each str is a sentence.
    num_keywords : int
        Number of keywords extracted from KR-WordRank
        Default is 100.
    stopwords : None or set of str
        Stopwords list for keyword and key-sentence extraction
    min_count : int
        Minimum frequency of subwords used to construct subword graph
        Default is 5
    max_length : int
        Maximum length of subwords used to construct subword graph
        Default is 10
    beta : float
        PageRank damping factor. 0 < beta < 1
        Default is 0.85
    max_iter : int
        Maximum number of iterations of HITS algorithm.
        Default is 10
    num_rset : int
        Number of R set words sorted by rank. It will be used to L-part word filtering.
        Default is -1.
    verbose : Boolean
        If True, it shows training status
        Default is False

    Returns
    -------
    keywords : dict
        Word : rank dictionary. keywords[str] = float

    Usage
    -----
        >>> from krwordrank.word import summarize_with_keywords

        >>> texts = [] # list of str
        >>> keywords = summarize_with_keywords(texts, num_keywords=100, min_count=5)
    """
    pass


class KRWordRank:
    """Unsupervised Korean Keyword Extractor

    Implementation of Kim, H. J., Cho, S., & Kang, P. (2014). KR-WordRank:
    An Unsupervised Korean Word Extraction Method Based on WordRank.
    Journal of Korean Institute of Industrial Engineers, 40(1), 18-33.

    Arguments
    ---------
    min_count : int
        Minimum frequency of subwords used to construct subword graph
        Default is 5
    max_length : int
        Maximum length of subwords used to construct subword graph
        Default is 10
    verbose : Boolean
        If True, it shows training status
        Default is False

    Examples
    -----
        >>> from krwordrank.word import KRWordRank

        >>> texts = ['예시 문장 입니다', '여러 문장의 list of str 입니다', ... ]
        >>> wordrank_extractor = KRWordRank()
        >>> keywords, rank, graph = wordrank_extractor.extract(texts, beta, max_iter, verbose)
    """

    def __init__(self, min_count=5, max_length=10, backend="auto", noun_only=True, verbose=False):
        self.min_count = min_count
        self.max_length = max_length
        self.verbose = verbose
        self.backend = backend
        self.noun_only = noun_only
        self.sum_weight = 1
        self.vocabulary = {}
        self.index2vocab = []

    def scan_vocabs(self, docs):
        """
        It scans subwords positioned of left-side (L) and right-side (R) of words.
        After scanning was done, KR-WordRank has index2vocab as class attribute.

        Arguments
        ---------
        docs : list of str
            Sentence list

        Returns
        -------
        counter : dict
            {(subword, 'L')] : frequency}
        """
        pass

    def _build_index2vocab(self):
        pass

    def extract(self, docs, beta=0.85, max_iter=10, num_keywords=-1,
                num_rset=-1, vocabulary=None, bias=None, rset=None):
        """
        It constructs word graph and trains ranks of each node using HITS algorithm.
        After training it selects suitable subwords as words.

        Arguments
        ---------
        docs : list of str
            Sentence list.
        beta : float
            PageRank damping factor. 0 < beta < 1
            Default is 0.85
        max_iter : int
            Maximum number of iterations of HITS algorithm.
            Default is 10
        num_keywords : int
            Number of keywords sorted by rank.
            Default is -1. If the vaule is negative, it returns all extracted words.
        num_rset : int
            Number of R set words sorted by rank. It will be used to L-part word filtering.
            Default is -1.
        vocabulary : None or dict
            User specified vocabulary to index mapper
        bias : None or dict
            User specified HITS bias term
        rset : None or dict
            User specfied R set

        Returns
        -------
        keywords : dict
            word : rank dictionary. {str:float}
        rank : dict
            subword : rank dictionary. {int:float}
        graph : dict of dict
            Adjacent subword graph. {int:{int:float}}

        Examples
        -----
            >>> from krwordrank.word import KRWordRank

            >>> texts = ['예시 문장 입니다', '여러 문장의 list of str 입니다', ... ]
            >>> wordrank_extractor = KRWordRank()
            >>> keywords, rank, graph = wordrank_extractor.extract(texts, beta, max_iter, verbose)
        """
        pass

    def train(self, docs, beta=0.85, max_iter=10, vocabulary=None, bias=None):
        """
        It constructs word graph and trains ranks of each node using HITS algorithm.
        Use this function only when you want to train rank of subwords

        Arguments
        ---------
        docs : list of str
            Sentence list.
        beta : float
            PageRank damping factor. 0 < beta < 1
            Default is 0.85
        max_iter : int
            Maximum number of iterations of HITS algorithm.
            Default is 10
        vocabulary : None or dict
            User specified vocabulary to index mapper
        bias : None or dict
            User specified HITS bias term
            {str: float} Format

        Returns
        -------
        rank : dict
            subword : rank dictionary. {int:float}
        graph : dict of dict
            Adjacent subword graph. {int:{int:float}}
        """
        pass

    def token2int(self, token):
        """
        Arguments
        ---------
        token : tuple
            (subword, 'L') or (subword, 'R')
            For example, ('이것', 'L') or ('은', 'R')

        Returns
        -------
        index : int
            Corresponding index
            If it is unknown, it returns -1
        """
        pass

    def int2token(self, index):
        """
        Arguments
        ---------
        index : int
            Token index

        Returns
        -------
        token : tuple
            Corresponding index formed such as (subword, 'L') or (subword, 'R')
            For example, ('이것', 'L') or ('은', 'R').
            If it is unknown, it returns None
        """
        pass

    def _construct_word_graph(self, docs):
        def normalize(graph):
            pass

        def rsub_to_token(t_left, t_curr):
            pass

        def token_to_lsub(t_curr, t_rigt):
            pass

        pass

    def _check_token(self, token_list):
        pass

    def _encode_token(self, token_list):
        pass

    def _intra_link(self, token):
        pass

    @staticmethod
    def _inter_link(tokens):
        pass

    @staticmethod
    def _filter_subtokens(keywords):
        pass

    @staticmethod
    def _select_keywords(lset, rset):
        pass

    @staticmethod
    def _filter_compounds(keywords):
        pass
