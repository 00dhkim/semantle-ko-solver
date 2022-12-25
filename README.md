# semantle-ko-solver

*꼬맨틀 솔버*

이 레포지토리는 NewsJelly의 꼬맨틀 - 단어 유사도 추측 게임(https://github.com/NewsJelly/semantle-ko)의 정답을 추측하는 솔버를 개발한 것입니다.

## setup

아래 링크를 통해 `valid_nearest.dat` 파일을 다운로드한 후 data/ 디렉토리에 담아주세요.

https://drive.google.com/file/d/1wEWHZzwwwRvfNyhJoCknJCzyPD-fJ9MH/view?usp=sharing

## requirements

- python 3
- `/data/valid_nearest.dat` file

## run

    python3 solver.py

## details

semantle-ko 게임은 `ko-aff-dic-0.7.92`와 `cc.ko.300.vec`의 두가지 데이터셋을 사용합니다. 두 데이터셋의 교집합 중 `smilegate-ai/kor_unsmile`에 의해 필터링된 59118 단어만을 정답 단어로 사용합니다.

단어들 중 유사도가 0.001 이하로 일치하는 단어만 반복하며
추출하여 정답 단어를 찾아냅니다.

일반적으로 2~3회 이내로 정답 단어를 찾아낼 수 있습니다.
