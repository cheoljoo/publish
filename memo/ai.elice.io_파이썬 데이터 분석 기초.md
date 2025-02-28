- description : ai 관련 교육 내용중 내가 모르던 것을 요약했다.  교육명 : 파이썬 데이터 분석 기초
- tag : ai, elice.io , python , data , analysis
- date : 2024-01-01

# 파이썬 데이터 분석 기초

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

- 
