# 파이썬 데이터 분석 기초 in https://elice.io/ko

## 01 트럼프 전 대통령 트윗으로 시작하는 데이터 처리
```python
# 문자열 모듈에서 특수문자를 처리를 돕는 메소드를 불러옵니다.
from string import punctuation
symbols = punctuation.replace('@', '').replace('#', '')
  # text에서 @와 #을 제외한 모든 특수문자를 제거합니다.
  for symbol in symbols:
    text = text.replace(symbol, '')
```

## 02 영어 단어 모음으로 시작하는 텍스트 파일 분석
- file read
```python
with open('data.txt','r') as file:
  for line in file
    contents.append(line.rstrip())
```

- list 코드 간략화하기
```python
even = [ n for n in numbers if n % 2 == 0]
```

- 그래프 다루기
  - matplotlib
    ```python
        # 막대 그래프의 막대 위치를 결정하는 pos를 선언합니다.
        pos = range(len(years))  # [0, 1, 2, 3, 4]
        
        # 높이가 온도인 막대 그래프를 그립니다.
        # 각 막대를 가운데 정렬합니다.
        plt.bar(pos, temperatures, align='center')
        
        # 각 막대에 해당되는 연도를 표기합니다.
        plt.xticks(pos, years)
        
        # 그래프를 엘리스 플랫폼 상에 표시합니다.
        plt.savefig('graph.png')
    ```

## 03 넷플릭스 시청 데이터로 알아보는 데이터형 변환

