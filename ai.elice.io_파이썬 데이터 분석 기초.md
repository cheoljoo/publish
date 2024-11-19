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
- set : ```합집합 | , 차집합 - , 교집합 & , XOR ^```
- matplotlib
```python
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 날짜 별 온도 데이터를 세팅합니다.
dates = ["1월 {}일".format(day) for day in range(1, 32)]
temperatures = list(range(1, 32))

# 막대 그래프의 막대 위치를 결정하는 pos를 선언합니다.
pos = range(len(dates))

# 한국어를 보기 좋게 표시할 수 있도록 폰트를 설정합니다.
font = fm.FontProperties(fname='./NanumBarunGothic.ttf')

# 막대의 높이가 빈도의 값이 되도록 설정합니다.
plt.bar(pos, temperatures, align='center')

# 각 막대에 해당되는 단어를 입력합니다.
plt.xticks(pos, dates, rotation='vertical', fontproperties=font)

# 그래프의 제목을 설정합니다.
plt.title('1월 중 기온 변화', fontproperties=font)

# Y축에 설명을 추가합니다.
plt.ylabel('온도', fontproperties=font)

# 단어가 잘리지 않도록 여백을 조정합니다.
plt.tight_layout()

# 그래프를 표시합니다.
plt.savefig('graph.png')
```
- netflix 작품 유사도
```python
def get_closeness(title_to_users, title1, title2):
    # title_to_users를 이용해 title1를 시청한 사용자의 집합을 저장합니다.
    title1_users = set(title_to_users[title1])
    # title_to_users를 이용해 title2를 시청한 사용자의 집합을 저장합니다.
    title2_users = set(title_to_users[title2])
    
    # 두 작품을 모두 본 사용자를 구합니다.
    both = len(title1_users & title2_users)
    # 두 작품 중 하나라도 본 사용자를 구합니다.
    either = len(title1_users | title2_users)

    return both / either
```

## 04 테드 강연으로 다뤄보는 복잡한 형태의 데이터
- 


