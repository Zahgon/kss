# Copyright (C) 2021 Hyunwoong Ko <kevin.brain@kakaobrain.com> and Sang Park <sang.park@dnotitia.com>
# All rights reserved.


from functools import lru_cache
from typing import Tuple

from kss._elements.subclasses import Syllable
from kss._modules.sentences.sentence_processor import SentenceProcessor
from kss._utils.const import sf_exception, jaum


class SentenceSplitter(SentenceProcessor):
    """
    Sentence Splitting Rules class

    Args:
        syllable (Syllable): current syllable
    """

    unavailable_next = set()
    unavailable_next.update({"시피", "거나", "의 "})
    unavailable_next.update({"에" + add for add in ["서", "선", "는", "도 "]})
    unavailable_next.update(
        {"라" + add for add in ["서", "는", "도 ", "던", "지만", "고", "건", "거나", "며", "면서"]}
    )
    unavailable_next.update(
        {"하" + add for add in ["여서", "여도", "였", "고는 ", "고서 ", "곤 ", "다는", "는데.", "며"]}
    )
    unavailable_next.update({"할" + add for add in ["텐데"]})

    def __init__(self, syllable: Syllable):
        super().__init__()
        self.syllable = syllable

    def __hash__(self):
        """Hash function for lru_cache"""
        return hash(self.syllable)

    ####################
    # Flow Controllers #
    ####################

    def check_split_start(self) -> bool:
        """
        Check whether the given syllable is split point or not.

        Returns:
            bool: whether the given syllable is split point or not.

        Notes:
            분할 시작 규칙:
                종결부호(SF), 캐릭터 휴리스틱 규칙, 4개의 어말어미(EF, EC, ETN, ETM) 규칙 중 하나라도 성립하면 분할한다.
        """
        pass

    def check_split_end(self) -> Tuple[bool, bool]:
        """
        Check whether the given syllable is split end point or not.

        Returns:
            bool: whether the given syllable is split end point or not.

        Notes:
            분할 종료 규칙:
                1. 현재 문자 이후의 문자가 자모(JAMO)이면 분할을 뒤로 미룬다.
                2. 현재 문자 이후의 문자가 대부분의 부호에 속하거나 현재 문자가 쉼표(,)인데 다음 문자도 쉼표(,)이면 분할을 뒤로 미룬다.
                3. 현재 문자 이후의 문자도 분할이 가능하면 분할을 뒤로 미룬다.
                4. 위 세가지 규칙에 해당 사항이 없는 경우 분할한다.

            예외:
                1. 만약 현재 문자가 물음표(?) 혹은 느낌표(!)인데 공백을 제외한 다음 문자가 구두점(.)이면 즉시 분할한다.
                2. 만약 현재 문자가 하이푼(-)인데 공백을 제외한 다음 문자가 종결부호(SF)가 아닌 경우 지금 즉시 분할한다.
                3. 만약 현재 문자가 자음인데 이전문자가 공백이고 다음 문자가 종결부호(SF)이며 다다음 문자가 공백이면 즉시 분할한다.
        """
        pass

    ###################
    # Splitting Rules #
    ###################

    def check_split_right_now(self) -> bool:
        """
        Check whether the given syllable is split end point or not.

        Returns:
            bool: whether the given syllable is split end point or not.

        Notes:
            단락기호(¶)가 등장하면 곧바로 분리한다.
        """
        pass

    def _sf(self) -> bool:
        """
        Check whether the given syllable is split end point or not.

        Returns:
            bool: whether the given syllable is split end point or not.

        Notes:
            종결부호 분할 규칙:
                종결부호(SF) 뒤에 공백(SP) 혹은 기타 부호(SY), 열린 괄호(SSO), 이모지(EMOJI), 한글 자모(JAMO)가 존재하면 분할한다.

            예외:
                1. 현재 문자 앞의 공백(SP)과 종결부호(SF)을 제외한 이전 문자가 숫자이면 분할하지 않는다.
                2. 현재 문자 앞의 공백(SP)과 종결부호(SF)을 제외한 문자가 긍정지정사(VCP)이면 분할하지 않는다.
                3. 현재 문자 앞의 공백(SP)과 종결부호(SF)을 제외한 문자가 조사(J*)이면서 다음 문자가 구두점(.)이면 분할하지 않는다.
                4. 현재 문자 뒤의 공백(SP)과 종결부호(SF)을 제외한 문자가 긍정지정사(VCP)이면 분할하지 않는다.
                5. 현재 문자 앞의 공백(SP)과 종결부호(SF)을 제외한 문자가 접속부사(MAJ)이면 분할하지 않는다.
                6. 현재 문자 앞의 공백(SP)과 종결부호(SF)을 제외한 문자가 '만', '데+..' 등 이면 분할하지 않는다.
                7. 현재 문자 뒤의 공백(SP)을 제외한 문자가 마침표(.)가 아니고 그 뒤 문자가 곧 바로 마침표라면 분할하지 않는다.
                8. 현재 문자 뒤로 등장하는 한글 문자열이 몇가지 분할하지 않아야 하는 경우에 속하면 분할하지 않는다.
                9. 현재 문자가 ' no.', ' No.', ' vol.', ' p.', ' pp.', ' page.', ' al.', ' ed.', ' eds.'
                    ' 항.', ' 조.', ' 호.', ' 절.', ' 권.', " 쪽.' 등에 존재하면 분할하지 않는다.
        """
        pass

    def _ef(self) -> bool:
        """
        Check whether the given syllable is split end point or not.

        Returns:
            bool: whether the given syllable is split end point or not.

        Notes:
            종결어미 분할 규칙:
                종결어미(EF)인 형태소의 마지막 문자이면 분할한다. 단, 현재 형태소에 조사(J*) 성분이 포함되면 분할하지 않는다.

            에외:
                1. 현재 문자 뒤의 공백(SP) 및 대부분 부호를 제외한 다음 문자가 쉼표(,)이면 분할하지 않는다. 단 ,,과 같이 연속되어 쓰이면 분할을 허용한다.
                2. 현재 문자 뒤의 공백(SP)을 제외한 다음 문자가 연결어미(EC), 조사(J*), 보조용언(VX) 중 하나이면 분할하지 않는다.
                3. 현재 형태소가 대명사(NP)+긍정지정사(VCP)+EF(종결어미)인데, 바로 뒤 문자가 종결부호(SF)가 아니면 분할하지 않는다.
                4. 현재 문자 바로 이전 문자가 공백(SP)이고 그 이전 문자가 보조용언(VX)이면 분할하지 않는다.
                5. 현재 문자 뒤로 등장하는 한글 문자열이 몇가지 분할하지 않아야 하는 경우에 속하면 분할하지 않는다.
        """
        pass

    def _ec(self) -> bool:
        """
        Check whether the given syllable is split end point or not.

        Returns:
            bool: whether the given syllable is split end point or not.

        Notes:
            연결어미 분할 규칙:
                연결어미(EC)인 형태소의 마지막 문자가 '다'일 때, 다음 허용항을 만족하면 분할한다.
                본래, 연결어미(EC)는 분할하면 안되지만, 형태소 분석기의 성능 문제로 종결어미(EF)를 연결어미(EC)로 인식되는 경우에 대응하기 위함이다.
                단, 현재 형태소에 조사(J*) 성분이 포함되면 분할하지 않는다.

            허용:
                1. 현재 문자의 이전 문자가 선어말어미(EP)이고 현재 문자의 뒤의 공백(SP)을 제외한 다음 문자가 닫는 괄호(SSO), 닫는 따옴표(QTO), 부호(SF, SY, EMOJI) 중 하나이면 분할한다.
                2. 현재 문자의 이전 문자가 선어말어미(EP)이고 현재 문자 뒤의 공백(SP)을 제외한 다음 문자가 대명사(NP) 혹은 접속부사(MAJ)이면 분할한다.
                3. 현재 문자의 이전 문자가 연결어미(EC)이면서 '니'인데, 뒤의 문자가 '만'이면서 연결어미(EC)가 아니면 분할한다. 이는 '입니다' 및 '습니다'가 연결어미로 인식되는 경우에 대응하기 위함이다.

            예외:
                1. 현재 문자 뒤의 공백(SP) 및 대부분 부호를 제외한 다음 문자가 쉼표(,)이면 분할하지 않는다. 단 ,,과 같이 연속되어 쓰이면 분할을 허용한다.
                2. 현재 문자 뒤의 공백(SP)을 제외한 다음 문자가 긍정지정사(VCP) 조사(J*), 보조용언(VX) 중 하나이면 분할하지 않는다.
                3. 현재 문자 뒤로 등장하는 한글 문자열이 몇가지 분할하지 않아야 하는 경우에 속하면 분할하지 않는다.
        """
        pass

    def _etn(self) -> bool:
        """
        Check whether the given syllable is split end point or not.

        Returns:
            bool: whether the given syllable is split end point or not.

        Notes:
            명사형 전성어미 분할 규칙:
                 명사형 전성어미(ETN)인 형태소의 마지막 문자가 '기'나 '길'이 아니면 분할한다.
                 이는 명사형 전성어미가 종결형으로 사용 될 경우에 대응 하기 위함이다. (~함, ~음, ~됨 등)
                 단, 현재 형태소에 조사(J*) 및 접미사(XS*) 성분이 포함되면 분할하지 않는다.

            예외:
                1. 현재 문자 뒤의 공백(SP) 및 대부분 부호를 제외한 다음 문자가 쉼표(,)이면 분할하지 않는다. 단 ,,과 같이 연속되어 쓰이면 분할을 허용한다.
                2. 현재 문자 뒤의 바로 뒤 문자가 공백, 한글 자모(JAMO), 이모지, 부호 등이 아니면 분할하지 않는다.
                3. 현재 문자 뒤의 공백(SP)을 제외한 다음 문자가 조사(J*), 동사(VV), 형용사(VA), 보조용언(VA) 이면 분할하지 않는다.
                4. 현재 문자 뒤의 공백(SP)과 종결부호(SF)를 제외한 다음 문자가 관형사(MM) 혹은 닫는 괄호(SSC)이면 분할하지 않는다.
                5. 현재 문자 뒤의 명사형 전성어미(ETN)을 제외한 이전의 문자와 동일한 문자가 현재 문자의 바로 뒤에 등장하면 분할하지 않는다.
                6. 현재 문자 뒤로 등장하는 한글 문자열이 몇가지 분할하지 않아야 하는 경우에 속하면 분할하지 않는다.
        """
        pass

    def _etm(self) -> bool:
        """
        Check whether the given syllable is split end point or not.

        Returns:
            bool: whether the given syllable is split end point or not.

        Notes:
            관형형 전성어미 분할 규칙:
                관형형 전성어미(ETM)인 형태소의 마지막 문자이면 다음 허용항을 만족하면 분할한다.
                이는 관형형 전성어미가 종결형으로 사용 될 경우에 대응 하기 위함이다. (~다능, ~했다던... 등)
                단, 현재 형태소에 조사(J*) 및 접미사(XS*) 성분이 포함되면 분할하지 않는다.

            허용:
                1. 이전 문자가 '다' 이면서 현재 문자가 '능'이면 분할한다.
                2. 현재 문자 뒤의 공백(SP)을 제외한 다음 문자가 말줄임표(SE)이면 분할한다.

            예외:
                1. 현재 문자의 뒤의 공백(SP) 및 대부분 부호를 제외한 다음 문자가 쉼표(,)이면 분할하지 않는다. 단 ,,과 같이 연속되어 쓰이면 분할을 허용한다.
                2. 현재 문자 뒤의 공백(SP) 및 대부분의 부호를 제외한 다음 문자가 의존명사(NNB)이면 분할하지 않는다.
                3. 현재 문자 뒤의 공백(SP)을 제외한 다음 문자가 조사(J*)이면 분할하지 않는다.
                4. 현재 문자 뒤로 등장하는 한글 문자열이 몇가지 분할하지 않아야 하는 경우에 속하면 분할하지 않는다.
        """
        pass

    def _char(self):
        """
        Check whether the given syllable is split end point or not.

        Returns:
            bool: whether the given syllable is split end point or not.

        Notes:
            캐릭터 기반의 휴리스틱 분할 규칙:
                캐릭터 기반의 문장분리 휴리스틱 알고리즘 적용한다.

            허용:
                듯 규칙 1. 현재 문자가 의존명사(NNB)이면서 '듯'이고 공백(SP) 종결부호(SF)를 제외한 다음 문자가 한글 자모(JAMO), 이모지(EMOJI), 말 줄임표(SE)
                        중 하나이면 현재 문자 뒤로 이어지는 모든 자모(JAMO) 및 이모지(EMOJI) 뒤의 문자가 동사가 아닌 경우 분할한다.
        """
        pass

    #####################
    # Utility functions #
    #####################

    @staticmethod
    def _tuple(exclude):
        pass

    @lru_cache(1)
    def _prev(self):
        pass

    @lru_cache(1)
    def _next(self):
        pass

    @lru_cache(30)
    def _prev_skip(
        self,
        poses=None,
        exclude=None,
    ):
        pass

    @lru_cache(30)
    def _next_skip(
        self,
        poses=None,
        exclude=None,
    ):
        pass

    @lru_cache(30)
    def _check_pos(
        self,
        poses=None,
        exclude=None,
    ):
        pass

    @lru_cache(30)
    def _check_text(
        self,
        texts=None,
        exclude=None,
    ):
        pass

    @lru_cache(30)
    def _check_next_pos(
        self,
        poses=None,
        exclude=None,
    ):
        pass

    @lru_cache(30)
    def _check_prev_pos(
        self,
        poses=None,
        exclude=None,
    ):
        pass

    @lru_cache(30)
    def _check_next_text(
        self,
        texts=None,
        exclude=None,
    ):
        pass

    @lru_cache(30)
    def _check_prev_text(
        self,
        texts=None,
        exclude=None,
    ):
        pass

    @lru_cache(30)
    def _check_next_skip_pos(
        self,
        poses=None,
        exclude=None,
        skip=None,
        skip_exclude=None,
    ):
        pass

    @lru_cache(30)
    def _check_prev_skip_pos(
        self,
        poses=None,
        exclude=None,
        skip=None,
        skip_exclude=None,
    ):
        pass

    @lru_cache(30)
    def _check_next_skip_text(
        self,
        texts=None,
        exclude=None,
        skip=None,
        skip_exclude=None,
    ):
        pass

    @lru_cache(30)
    def _check_prev_skip_text(
        self,
        texts=None,
        exclude=None,
        skip=None,
        skip_exclude=None,
    ):
        pass

    @lru_cache(30)
    def _check_next_skip_sp_pos(
        self,
        poses=None,
        exclude=None,
    ):
        pass

    @lru_cache(30)
    def _check_next_skip_from_current_pos(
        self,
        poses=None,
        exclude=None,
    ):
        pass

    @lru_cache(30)
    def _check_prev_skip_sp_pos(
        self,
        poses=None,
        exclude=None,
    ):
        pass

    @lru_cache(30)
    def _check_next_skip_spsf_pos(
        self,
        poses=None,
        exclude=None,
    ):
        pass

    @lru_cache(30)
    def _check_prev_skip_spsf_pos(
        self,
        poses=None,
        exclude=None,
    ):
        pass

    @lru_cache(30)
    def _check_next_skip_sp_text(
        self,
        texts=None,
        exclude=None,
    ):
        pass

    @lru_cache(30)
    def _check_prev_skip_sp_text(
        self,
        texts=None,
        exclude=None,
    ):
        pass

    @lru_cache(30)
    def _check_next_skip_spsf_text(
        self,
        texts=None,
        exclude=None,
    ):
        pass

    @lru_cache(30)
    def _check_prev_skip_spsf_text(
        self,
        texts=None,
        exclude=None,
    ):
        pass

    @lru_cache(30)
    def _check_next_skip_all_s_pos(
        self,
        poses=None,
        exclude=None,
    ):
        pass

    @lru_cache(30)
    def _check_next_skip_all_s_text(
        self,
        texts=None,
        exclude=None,
    ):
        pass

    @lru_cache(30)
    def _check_texts(self, texts=None):
        pass

    @lru_cache(30)
    def _check_prev_texts(self, texts=None):
        pass

    @lru_cache(30)
    def _check_next_skip_all_s_texts(self, texts=None):
        pass

    @lru_cache(30)
    def _check_next_skip_all_s_multiple_texts(self, *texts):
        pass

    @lru_cache(1)
    def _check_next_is_unavailable_split(self):
        pass

    @lru_cache(1)
    def _check_non_doubled_comma(self):
        pass

    @lru_cache(30)
    def _check_prev_texts_from_before(self, text):
        pass

    @lru_cache(30)
    def _check_multiple_prev_texts_from_before(self, *texts):
        pass

    @lru_cache(30)
    def _check_multiple_next_texts_from_current(self, *texts):
        pass
