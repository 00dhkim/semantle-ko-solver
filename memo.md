# memo.md

semantle-ko 프로젝트의 처리 흐름을 요약하기 위한 자료

## 도커 흐름

파일은 수정하는 즉시 컨테이너 내부에 적용됨

단, html 파일은 플라스크 앱인 `semantle.py` 파일을 재실행해야 변경된 html이 렌더링됨

## 파일 생성 전처리 흐름

1. `filter_words.py`에서 `frequent_words.txt` 파일로 `filtered_frequent_words.txt` 파일 생성
2. `process_vecs.py`에서 `cc.ko.300.vec` 파일로 `valid_guesses.db` 파일과 `valid_nearest.dat` 파일 생성
3. `generate_secrets.py`에서 `filtered_frequent_words.txt` 파일로 `secrets.txt` 파일 생성
4. (전처리 끝)

## data 파일의 구성

- `secrets.txt`
    - 하루 1단어.
    - 비밀단어로 사용할 단어들을 미리 지정함.
- `frequent_words.txt`
    - 5472단어.
- `filtered_frequent_words.txt`
    - 5370단어.
    - frequent_words.txt에서 부정적인 단어를 필터링한 단어들.
- `ko-aff-dic-0.7.92/ko.dic`
    - 101454단어.
- `ko-aff-dic-0.7.92/ko_filtered.txt`
    - 96072단어.
    - ko.dic 파일에서 부정적인 단어를 필터링한 단어들.
- `valid_guesses.db`
    - 1505619단어.
    - cc.ko.300.vec에서 추출됨.
    - 여기에 있는 단어만 추측하기 가능.
    - (word, vec) 쌍으로 구성됨. vec은 리스트 객체의 dump.
    - 단어간 유사도 계산 시 vec 가져오는 데 사용.
- `valid_nearest.dat`
    - 59118단어.
    - valid_nearest_words 및 valid_nearest_vecs 리스트를 담는 파이썬 객체.
    - ko_filtered.txt의 단어와 valid_guesses.db의 교집합만 담김.
    - 여기있는 단어만 유사도 순위에 나타남.

전처리가 끝나면 `valid_guesses.db`와 `valid_nearest.dat`만 쓰임