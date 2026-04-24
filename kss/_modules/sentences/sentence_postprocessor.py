# Copyright (C) 2021 Hyunwoong Ko <kevin.brain@kakaobrain.com> and Sang Park <sang.park@dnotitia.com>
# All rights reserved.


from typing import List

from kss._elements.subclasses import Syllable
from kss._modules.sentences.sentence_preprocessor import SentenceProcessor
from kss._utils.const import quotes_or_brackets_close_to_open, spaces, daggers


class SentencePostprocessor(SentenceProcessor):
    def postprocess(
        self,
        output_sentences: List[List[Syllable]],
        strip: bool,
    ) -> List[str]:
        """
        Postprocess output sentences by splitting rules

        Args:
            output_sentences (List[List[Syllable]]): output sentences by splitting rules in syllable object
            strip (bool): strip all sentences or not

        Returns:
            List[str]: postprocessed output setences in string
        """
        pass

    def _merge_broken_sub_sentence_in_quotes_or_brackets(
        self, output_sentences: List[List[Syllable]]
    ) -> List[List[Syllable]]:
        """
        Merge broken sub-sentence in quotes or brackets.

        Args:
            output_sentences (List[List[Syllable]]): list of syllables

        Returns:
            List[List[Syllable]]: corrected list of syllables.

        Notes:
            열고 닫음이 분명한 괄호나 따옴표 안의 인용문/독백 등이 분리 된 경우 이를 찾아내서 병합한다.

            예시:
                입력: ["나는 생각했다. ", "(분명히 맞을 것이다. ", "그래야만 한다.) ", "그리곤 말했다."]
                출력: ["나는 생각했다. ", "(분명히 맞을 것이다. 그래야만 한다.) ", "그리곤 말했다."]
        """
        pass

    @staticmethod
    def _check_text_from_character(output_syllable: Syllable, target: str):
        """
        Check given text is matched from character

        Args:
            output_syllable (Syllable): output syllable
            target (str): target string

        Returns:
            bool: match or not
        """
        pass

    def _move_first_daggers_in_sentence_to_previous(
        self, output_sentences: List[List[Syllable]]
    ) -> List[List[Syllable]]:
        """
        Move first daggers in sentence to previous.

        Args:
            output_sentences (List[List[Syllable]]): list of syllables

        Returns:
            List[List[Syllable]]: corrected list of syllables.

        Notes:
            칼표 처리:
                칼표가 처음으로 등장한 문장의 이전문장이 행갈이나 공백으로 끝난게 아니라면 칼표를 이전 문장으로 옮긴다.

            예시:
                입력: ["GPT3는 인공지능 모델이다.", "† 그러나 이 모델은""]
                출력: ["GPT3는 인공지능 모델이다.†", "그러나 이 모델은""] <--- 본문에 쓰인 각주로 인식.

                입력: ["GPT3는 인공지능 모델이다.\n", "† 그러나 이 모델은""]
                출력: ["GPT3는 인공지능 모델이다.\n", "† 그러나 이 모델은""]  <--- footer에 쓰인 각주로 인식. (그대로 유지)

                입력: ["GPT3는 인공지능 모델이다. ", "† 그러나 이 모델은""]
                출력: ["GPT3는 인공지능 모델이다. ", "† 그러나 이 모델은""]  <--- footer에 쓰인 각주로 인식. (그대로 유지)
        """
        pass

    def _move_symbol_sentences_only_to_previous(
        self, output_sentences: List[List[Syllable]]
    ) -> List[List[Syllable]]:
        """
        Move symbol only sentences to previous

        Args:
            output_sentences (List[List[Syllable]]): list of syllables

        Returns:
            List[List[Syllable]]: corrected list of syllables.

        Notes:
            Symbol 처리:
                Symbol로만 이루어진 문장을 이전 문장으로 옮긴다.
        """
        pass

    def _move_first_footnote_in_sentence_to_previous(
        self, output_sentences: List[List[Syllable]]
    ) -> List[List[Syllable]]:
        """
        Move first footnote in sentence to previous.

        Args:
            output_sentences (List[List[Syllable]]): list of syllables

        Returns:
            List[List[Syllable]]: corrected list of syllables.

        Notes:
            각주 처리:
                최초로 발견되는 대괄호('[') 안에 있는 것이 각주이면 이를 이전 문장으로 옮긴다.

            예시:
                입력: ["그것은 사실이였다.", "[13] 하지만 그에 따라"]
                출력: ["그것은 사실이였다.[13]", "하지만 그에 따라"]

                출력: ["그것은 사실이였다.", "[편집]하지만 그에 따라"]
                출력: ["그것은 사실이였다.[편집]", "하지만 그에 따라"]

                출력: ["그것은 사실이였다.", "[편집]을 하고 싶지만 그에 따라"]
                출력: ["그것은 사실이였다.", "[편집]을 하고 싶지만 그에 따라"] <--- 유지

                출력: ["그것은 사실이였다.", "[더 보기] 마침 좋은 생각이 떠올랐다."]
                출력: ["그것은 사실이였다.[더 보기]", "마침 좋은 생각이 떠올랐다."]

                출력: ["그것은 사실이였다.", "[더 보기] 버튼을 눌러보세요."]
                출력: ["그것은 사실이였다.", "[더 보기] 버튼을 눌러보세요."] <--- 유지

                출력: ["그것은 사실이였다.", "[사각형]은"]
                출력: ["그것은 사실이였다.", "[사각형]은"] <--- 유지
        """
        pass

    def _move_non_structural_sub_sent_in_brackets_to_previous(
        self, output_sentences: List[List[Syllable]]
    ) -> List[List[Syllable]]:
        """
        Move non-structural sub sentence in brackets to previous.

        Args:
            output_sentences (List[List[Syllable]]): list of syllables

        Returns:
            List[List[Syllable]]: corrected list of syllables.

        Notes:
            최초로 발견되는 괄호('(') 안의 서브 문장이 명사(N*)로 끝나면서 공백을 제외한 다음 문자가
            조사(J*)가 아니라면 잘못 분리된 것으로 간주하고 이를 이전 문장으로 옮긴다.

            예시:
                입력: ["아니거든 !!! ", "(강한부정) 너가 먼자 말했잖아!"]
                출력: ["아니거든 !!! (강한부정)", " 너가 먼자 말했잖아!"]
        """
        pass

    def _move_unexpected_split_sentences_to_previous(
        self, output_sentences: List[List[Syllable]]
    ) -> List[List[Syllable]]:
        """
        Move unexpected split sentences to previous.

        Args:
            output_sentences (List[List[Syllable]]): list of syllables

        Returns:
            List[List[Syllable]]: corrected list of syllables.

        Notes:
            분리된 문장이 조사(J*), 긍정지정사(VCP), 연결어미(EC), 보조용언(VX)으로 시작되면 이전 문장에 이어 붙인다.
            또는 문장이 칼표나 겹칼표 등의 주석 문자로 시작 했을때 다음 문자가 공백이 아니면

            예시:
                입력: ['반드시 막아야만 한다', '라고 했다']
                출력: ['반드시 막아야만 한다라고 했다']

                입력: ['반드시 막아야만 한다', '라고 했다']
                출력: ['반드시 막아야만 한다라고 했다']
        """
        pass

    @staticmethod
    def _convert_syllables_to_sentences_with_cleaning(
        output_sentences: List[List[Syllable]],
        strip: bool,
    ) -> List[str]:
        """
        Convert syllables to sentences with cleaning

        Args:
            output_sentences (List[List[Syllable]]): output syllables
            strip (bool): strip all sentences or not

        Returns:
            List[str]: output sentences list

        Notes:
            Syllable 객체를 모두 string으로 변경하고 각 문장에 strip을 수행한다.
        """
        pass

    @staticmethod
    def _remove_empty_sentence(output_sentences: List[List[Syllable]]):
        """
        Remove emtpy sentences after postprocessing

        Args:
            output_sentences (List[List[Syllable]]): split list of syllables

        Returns:
            List[List[Syllable]]: list of syllables without empty one
        """
        pass

    @staticmethod
    def _remove_space_before_emoji(
        output_sentences: List[List[Syllable]],
    ) -> List[List[Syllable]]:
        """
        Remove a space character before emoji.
        The space character was appended in preprocessing step.

        Args:
            output_sentences (List[List[Syllable]]): split list of syllables

        Returns:
            List[List[Syllable]]: list of syllables without space before emoji
        """
        pass

    @staticmethod
    def _remove_first_space(
        output_sentences: List[List[Syllable]],
    ) -> List[List[Syllable]]:
        """
        Remove a space added by preprocessor

        Args:
            output_sentences (List[List[Syllable]]): split list of syllables

        Returns:
            List[List[Syllable]]: list of syllables without added space
        """
        pass
