"""
solver.py

solver for semantle-ko: https://github.com/NewsJelly/semantle-ko

ko-aff-dic-0.7.92와 cc.ko.300.vec의 교집합 중 smilegate-ai/kor_unsmile에 의해
필터링된 59118 단어 중에서 유사도가 0.001 이하로 일치하는 단어만 반복하여
추출하여 정답 단어를 찾아냄.

"""

import pickle
import random

import word2vec


class Solver:
    """solver class for semantle-ko"""

    def __init__(self):
        self._valid_nearest_words, self._valid_nearest_vecs = self.load_dat()
        self.words = self.gen_words()

    def load_dat(self):
        """valid_nearest_words와 valid_nearest_vecs 객체를 불러옴."""
        with open('data/valid_nearest.dat', 'rb') as f:
            return pickle.load(f)

    def gen_words(self):
        """valid_nearest.dat에서 불러온 단어와 벡터를 words 리스트에 저장함."""
        assert len(self._valid_nearest_words) == len(self._valid_nearest_vecs)
        length = len(self._valid_nearest_vecs)
        words = []
        for idx, word, vec in zip(range(length), \
                                  self._valid_nearest_words, self._valid_nearest_vecs):
            words.append({
                'valid': True,
                'idx': idx,
                'text': word,
                'vec': vec,
            })
        return words

    def guess(self, is_random=True) -> bool:
        """단어를 추측하고 유사도를 입력하면 정답 여부를 반환함.

        Args:
            is_random (bool, optional): True이면 solver가 랜덤으로 단어를 지정해줌.
            False이면 사용자가 단어를 직접 고름. Defaults to True.
        """

        if is_random:
            guess_word = random.choice(self.words)
            print(f'guess word: {guess_word["text"]}')
        else:
            guess_word_text = input('guess word: ')
            guess_word = self.words[self._valid_nearest_words.index(
                guess_word_text)]

        guess_similarity = float(input('guess similarity (float type): '))

        for word in self.words:
            if not word['valid']:
                continue

            word_similarity = word2vec.cosine_similarity(
                guess_word['vec'], word['vec'])
            if abs(guess_similarity - word_similarity) > 0.001:
                word['valid'] = False
            else:
                # 예상 답변 후보 출력
                # print(f'valid: {word["text"]}, similarity: {word_similarity}')
                pass

        if self.count_valid() == 1:
            print(f'\nanswer: {self.get_answer()["text"]}')
            return True
        else:
            print(f'valid words: {self.count_valid()}, try again\n')
            return False

    def count_valid(self) -> int:
        """self.words에서 valid가 True인 단어의 개수를 반환함."""
        return sum(word['valid'] for word in self.words)

    def get_answer(self) -> dict:
        """self.words에서 valid가 하나일 때 그 단어를 반환함."""
        assert self.count_valid() == 1
        return next(word for word in self.words if word['valid'])


if __name__ == '__main__':
    solver = Solver()
    while True:
        if solver.guess():
            break
