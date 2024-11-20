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

- final
```python
# 트럼프 전 대통령의 트윗 모음을 불러옵니다.
from tweets import trump_tweets

# 분석에서 제외하기 위한 불용어 모음을 불러옵니다.
from stopwords import stopwords

# 그래프에 필요한 라이브러리를 불러옵니다. 
import matplotlib.pyplot as plt

# 단어구름에 필요한 라이브러리를 불러옵니다. 
import numpy as np
from PIL import Image
from wordcloud import WordCloud

# 특화된 컨테이너 모듈에서 수 세기를 돕는 메소드를 불러옵니다.
from collections import Counter

# 문자열 모듈에서 특수문자를 처리를 돕는 메소드를 불러옵니다. 
from string import punctuation

# 엘리스에서 파일 송출에 필요한 패키지를 불러옵니다. 
from elice_utils import EliceUtils
elice_utils = EliceUtils()


# 데이터 전처리를 실행합니다. 
def preprocess_text(text):
    # 분석을 위해 text를 모두 소문자로 변환합니다.
    text = text.lower()
    
    # @와 #을 제외한 특수문자로 이루어진 문자열 symbols를 만듭니다.

    symbols = punctuation.replace('@', '').replace('#', '')
    
    # text에서 @와 #을 제외한 모든 특수문자를 제거합니다.
    for symbol in symbols:
        text = text.replace(symbol, '')
    
    # # text를 띄어쓰기 단위로 쪼갭니다.
    # words = text.split()
    # return words

    symbols = ''
    for s in text:
        # if '0' <= s <= '9' or 'a' <= s <= 'z' or s == ' ' or s == '\t' or s == '\n':
        if '0' <= s <= '9' or 'a' <= s <= 'z' or s == '#' or s == '@' or s == ' ' or s == '\t' or s == '\n':
            symbols += s
    
    # print('symbols:',symbols)
    return symbols.split()
    

# 해시태그와 키워드를 추출합니다. 
def analyze_text(words):
    # 키워드, 해시태그, 멘션을 저장할 리스트를 각각 생성합니다.
    keywords, hashtags, mentions = [], [], []
    for word in words:
        if word.startswith('@'):
            mentions.append(word[1:])
            keywords.append(word[1:])
        elif word.startswith('#'):
            hashtags.append(word[1:])
            keywords.append(word[1:])
        else :
            keywords.append(word)
    
    return keywords, hashtags, mentions


def filter_by_month(tweet_data, month):
    # month를 문자열로 바꾼 month_string을 선언합니다.
    # 이 때 한 자리 수는 앞에 '0'을 넣어줍니다. (ex: 1 => '01')
    month_string = '0' + str(month) if month < 10 else str(month)
    
    # 선택한 달의 트윗을 filtered_tweets에 저장합니다.
    filtered_tweets = []
    for d,t in tweet_data:
        if d.startswith(month_string):
            filtered_tweets.append(t)
    
    # 트윗의 날짜가 선택한 달에 속해 있으면 트윗의 내용을 filtered_tweets에 추가합니다.
    return filtered_tweets


# 트윗 통계를 출력합니다.
def show_stats():
    keyword_counter = Counter()
    hashtag_counter = Counter()
    mention_counter = Counter()
    
    for _, tweet in trump_tweets:
        keyward, hashtag, mention = analyze_text(preprocess_text(tweet))
        keyword_counter += Counter(keyward)
        hashtag_counter += Counter(hashtag)
        mention_counter += Counter(mention)
    
    # 가장 많이 등장한 키워드, 해시태그, 멘션을 출력합니다.
    top_ten = hashtag_counter.most_common(10)
    for hashtag, freq in top_ten:
        print('{}: {}회'.format(hashtag, freq))


# 월 별 트윗 개수를 보여주는 그래프를 출력합니다. 
def show_tweets_by_month():
    months = range(1, 13)
    num_tweets = [len(filter_by_month(trump_tweets, month)) for month in months]
    
    plt.bar(months, num_tweets, align='center')
    plt.xticks(months, months)
    
    plt.savefig('graph.png')
    elice_utils = EliceUtils()
    elice_utils.send_image('graph.png')


# wordcloud 패키지를 이용해 트럼프 대통령 실루엣 모양의 단어구름을 생성합니다.
def create_word_cloud():
    
    counter = Counter()
    for _, tweet in trump_tweets:
        keywords, _, _ = analyze_text(preprocess_text(tweet))
        counter += Counter(keywords)
    
    trump_mask = np.array(Image.open('trump.png'))
    cloud = WordCloud(background_color='white', mask=trump_mask)
    cloud.fit_words(counter)
    cloud.to_file('cloud.png')
    elice_utils.send_image('cloud.png')


# 입력값에 따라 출력할 결과를 선택합니다. 
def main(code=1):
    # 가장 많이 등장한 키워드, 해시태그, 멘션을 출력합니다.
    if code == 1:
        show_stats()
    
    # 트럼프 전 대통령의 월별 트윗 개수 그래프를 출력합니다.
    if code == 2:
        show_tweets_by_month()
    
    # 트럼프 전 대통령의 트윗 키워드로 단어구름을 그립니다.
    if code == 3:
        create_word_cloud()


# main 함수를 실행합니다. 
if __name__ == '__main__':
    main(3)
    result = preprocess_text("On my way! #Inauguration2017 https://t.co/hOuMbxGnpe")
    print(result)  # ['on', 'my', 'way', '#inauguration2017', 'httpstcohoumbxgnpe']
    result = preprocess_text("Hello World!! @user #Python3")
    print(result)  # ['hello', 'world', 'user', 'python3']

    result = preprocess_text("Check this out! #Amazing @friend :)")
    print(result)  # ['check', 'this', 'out', 'amazing', 'friend']
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
    
- final
```python
# 프로젝트에 필요한 패키지를 import합니다.
from operator import itemgetter
from collections import Counter
from string import punctuation
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

from elice_utils import EliceUtils
elice_utils = EliceUtils()


def import_corpus(filename):
    # 튜플을 저장할 리스트를 생성합니다.
    corpus = []
    
    # 매개변수로 입력 받은 파일을 열고 읽습니다.
    with open(filename,'r') as fd:
        # 텍스트 파일의 각 줄을 (단어, 빈도수) 꼴로 corpus에 저장합니다.
        for line in fd:
            # print(line)
            a = line.split(',')
            corpus.append( (a[0],int(a[1])) )
    return corpus


def create_corpus(filenames):
    # 단어를 저장할 리스트를 생성합니다.
    words = []
    
    # 여러 파일에 등장하는 모든 단어를 모두 words에 저장합니다.
    for filename in filenames:
        with open(filename,'r') as fd:
            for line in fd:
                for symbol in punctuation:
                    line = line.replace(symbol,'')
                words += line.strip().split()
            
            # 이 때 문장부호를 포함한 모든 특수기호를 제거합니다. 4번째 줄에서 임포트한 punctuation을  이용하세요.
            # for symbol in punctuation:
            #     content = None
            # words = None
    
    # words 리스트의 데이터를 corpus 형태로 변환합니다. Counter() 사용 방법을 검색해보세요.
    corpus = Counter(words)
    return list(corpus.items())


def filter_by_prefix(corpus, prefix):
    return [ i for i in corpus if i[0].startswith(prefix)]


def most_frequent_words(corpus, number):
    return sorted(corpus,key=lambda item:item[1],reverse=True)[:number]
    

def draw_frequency_graph(corpus):
    # 막대 그래프의 막대 위치를 결정하는 pos를 선언합니다.
    pos = range(len(corpus))
    
    # 튜플의 리스트인 corpus를 단어의 리스트 words와 빈도의 리스트 freqs로 분리합니다.
    words = [tup[0] for tup in corpus]
    freqs = [tup[1] for tup in corpus]
    
    # 한국어를 보기 좋게 표시할 수 있도록 폰트를 설정합니다.
    font = fm.FontProperties(fname='./NanumBarunGothic.ttf')
    
    # 막대의 높이가 빈도의 값이 되도록 설정합니다.
    plt.bar(pos, freqs, align='center')
    
    # 각 막대에 해당되는 단어를 입력합니다.
    plt.xticks(pos, words, rotation='vertical', fontproperties=font)
    
    # 그래프의 제목을 설정합니다.
    plt.title('단어 별 사용 빈도', fontproperties=font)
    
    # Y축에 설명을 추가합니다.
    plt.ylabel('빈도', fontproperties=font)
    
    # 단어가 잘리지 않도록 여백을 조정합니다.
    plt.tight_layout()
    
    # 그래프를 표시합니다.
    plt.savefig('graph.png')
    elice_utils.send_image('graph.png')


def main(prefix=''):
    # import_corpus() 함수를 통해 튜플의 리스트를 생성합니다.
    corpus = import_corpus('corpus.txt')
    
    # head로 시작하는 단어들만 골라 냅니다.
    prefix_words = filter_by_prefix(corpus, prefix)
    print('prefix_words',prefix,prefix_words[:50])
    
    # 주어진 prefix로 시작하는 단어들을 빈도가 높은 순으로 정렬한 뒤 앞의 10개만 추립니다.
    top_ten = most_frequent_words(prefix_words, 10)
    print('top_ten',top_ten)
    
    # 단어 별 빈도수를 그래프로 나타냅니다.
    draw_frequency_graph(top_ten)
    
    # 'Alice in Wonderland' 책의 단어를 corpus로 바꿉니다.
    alice_files = ['alice/chapter{}.txt'.format(chapter) for chapter in range(1, 6)]
    alice_corpus = create_corpus(alice_files)
    
    top_ten_alice = most_frequent_words(alice_corpus, 10)
    draw_frequency_graph(top_ten_alice)


if __name__ == '__main__':
    main()
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

- final
```python
import matplotlib.pyplot as plt
import json
from operator import itemgetter

from elice_utils import EliceUtils
from movies import titles


def preprocess_data(filename):
    processed = {}
    with open(filename) as file:
        # 입력 받은 JSON 파일을 불러와 loaded에 저장합니다.
        loaded = json.load(file)
        # JSON 형식의 데이터에서 영화와 사용자 정보를 하나씩 가져옵니다.
        for k,v in loaded.items():
            # processed 딕셔너리에 title을 키로, user를 값으로 저장합니다.
            processed[int(k)] = v  # 영화id(int) : [유저id]
            
                
        return processed


def reformat_data(title_to_users):
    user_to_titles = {}
    # 입력받은 딕셔너리에서 영화와 사용자 정보를 하나씩 가져옵니다.
    # print('ref',title_to_users.keys())
    for title,users in title_to_users.items():
        # user_to_titles에 사용자 정보가 있을 경우 사용자의 영화 정보를 추가합니다. 이때 영화 정보는 리스트형으로 저장됩니다. 
        for user in users:
            if user in user_to_titles:
                user_to_titles[user].append(title)
            else :
                user_to_titles[user] = [title] 
        
            
                
            # user_to_titles에 사용자 정보가 없을 경우 사용자 정보와 영화 정보를 추가합니다. 이때 영화 정보는 리스트형으로 저장됩니다. 
            
                
    
    return user_to_titles


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


def predict_preference(title_to_users, user_to_titles, user, title):
    # user_to_titles를 이용해 user가 시청한 영화를 저장합니다.
    titles = user_to_titles[user]
    # get_closeness() 함수를 이용해 유사도를 계산합니다.
    closeness = []
    for utitle in titles:
        closeness.append(get_closeness(title_to_users, utitle, title))

    return sum(closeness) / len(closeness)


def main():
    filename = 'netflix.json'
    title_to_users = preprocess_data(filename)
    user_to_titles = reformat_data(title_to_users)
    
    lotr1 = 2452                # 반지의 제왕 - 반지 원정대
    lotr2 = 11521               # 반지의 제왕 - 두 개의 탑
    lotr3 = 14240               # 반지의 제왕 - 왕의 귀환
    
    killbill1 = 14454           # 킬 빌 - 1부
    killbill2 = 457             # 킬 빌 - 2부
    
    jurassic_park = 14312       # 쥬라기 공원
    shawshank = 14550           # 쇼생크 탈출
    
    print("[유사도 측정]")
    #값을 바꿔가며 실행해보세요.
    title1 = lotr1
    title2 = killbill1
    description = "{}와 {}의 작품 성향 유사도".format(titles[title1], titles[title2])
    closeness = round(get_closeness(title_to_users, title1, title2) * 100)
    print("{}: {}%".format(description, closeness))
    
    username = 'elice'
    new_utt = user_to_titles.copy()
    new_utt[username] = [lotr1, lotr2, lotr3]
    
    # print('titles:',title_to_users.keys())
    print("[{} 사용자를 위한 작품 추천]".format(username))
    preferences = [(title, predict_preference(title_to_users, new_utt, 'elice', title)) for title in title_to_users]
    preferences.sort(key=itemgetter(1), reverse=True)
    for p in preferences[:10]:
        print("{} ({}%)".format(titles[p[0]], round(p[1] * 100)))


if __name__ == "__main__":
    main()
```


## 04 테드 강연으로 다뤄보는 복잡한 형태의 데이터
- lambda
  - ```square = lambda x : x*x```
  - 예제
    ```python
    >>> from operator import itemgetter
    >>> get_zeroth = itemgetter(0)
    >>> numbers = [1, 2, 3]
    >>> print(get_zeroth(numbers))
    1
    # ----
    def adder(n):
        def helper(x):
            return x + n
        return helper
    
    add_three = adder(3)
    print(add_three(6)) # 9
    ```
- map
  - map(func , data_argument)
  - lazy
    ```python
    eng_title = map(get_eng_title,movies)
    print(eng_titles)   # <map object at ...>
    ```
    - eng_title[0]라고 해야 실행되어진다. 위에서는 그냥 map형식으로 선언만 된 것이다. 실제로 data를 얻으려 할때 사용되는 것이다.
    - movies의 각 값이 get_eng_title의 인자로 들어간다.
- filter
  - map과 같은 형식으로 수행되나, 함수의 값이 True일때만 처리
  - lazy 처리

- final
```python
"""
['8',
'With more than half of the world population living in cities, one thing is undeniable: we are an urban species. Part game, part urban planning sketching tool, "Cities: Skylines" encourages people to use their creativity and self-expression to rethink the cities of tomorrow. Designer Karoliina Korppoo takes us on a tour through some extraordinary places users have created, from futuristic fantasy cities to remarkably realistic landscapes. What does your dream city look like?',
    '519',
    'TED2017',
    '1492992000',
    '1',
    'Karoliina Korppoo',
    'Karoliina Korppoo: How a video game might help us build better cities',
    '1',
    '1506092422',
    "[{'id': 21, 'name': 'Unconvincing', 'count': 21}, {'id': 8, 'name': 'Informative', 'count': 25}, {'id': 10, 'name': 'Inspiring', 'count': 26}, {'id': 25, 'name': 'OK', 'count': 11}, {'id': 22, 'name': 'Fascinating', 'count': 9}, {'id': 9, 'name': 'Ingenious', 'count': 14}, {'id': 2, 'name': 'Confusing', 'count': 3}, {'id': 26, 'name': 'Obnoxious', 'count': 4}, {'id': 1, 'name': 'Beautiful', 'count': 12}, {'id': 11, 'name': 'Longwinded', 'count': 9}, {'id': 24, 'name': 'Persuasive', 'count': 5}, {'id': 23, 'name': 'Jaw-dropping', 'count': 3}, {'id': 3, 'name': 'Courageous', 'count': 0}, {'id': 7, 'name': 'Funny', 'count': 0}]",
    "[{'id': 2682, 'hero': 'https://pe.tedcdn.com/images/ted/5344a548b578587ac392c3e05e0e604f55371d94_2880x1620.jpg', 'speaker': 'Jeff Speck', 'title': '4 ways to make a city more walkable', 'duration': 1117, 'slug': 'jeff_speck_4_ways_to_make_a_city_more_walkable', 'viewed_count': 1354747}, {'id': 2839, 'hero': 'https://pe.tedcdn.com/images/ted/7651fdc16fac4fe5a41e91a65ee168af109e227e_2880x1620.jpg', 'speaker': 'Peter Calthorpe', 'title': '7 principles for building better cities', 'duration': 860, 'slug': 'peter_calthorpe_7_principles_for_building_better_cities', 'viewed_count': 834219}, {'id': 1501, 'hero': 'https://pe.tedcdn.com/images/ted/1524765b73f465b35cdf9c4689674a42bdd5a917_1600x1200.jpg', 'speaker': 'Jane McGonigal', 'title': 'The game that can give you 10 extra years of life', 'duration': 1170, 'slug': 'jane_mcgonigal_the_game_that_can_give_you_10_extra_years_of_life', 'viewed_count': 6141800}, {'id': 1429, 'hero': 'https://pe.tedcdn.com/images/ted/f45ba92c04bdaedad7cf56e5182efb7953516601_800x600.jpg', 'speaker': 'Eduardo Paes', 'title': 'The 4 commandments of cities', 'duration': 741, 'slug': 'eduardo_paes_the_4_commandments_of_cities', 'viewed_count': 834941}, {'id': 1865, 'hero': 'https://pe.tedcdn.com/images/ted/34113888f29018d7f07a3c7f10ab2915c50f6b96_1600x1200.jpg', 'speaker': 'Mick Cornett', 'title': 'How an obese town lost a million pounds', 'duration': 915, 'slug': 'mick_cornett_how_an_obese_town_lost_a_million_pounds', 'viewed_count': 1514949}, {'id': 213, 'hero': 'https://pe.tedcdn.com/images/ted/28410_480x360.jpg', 'speaker': 'Jaime Lerner', 'title': 'A song of the city', 'duration': 943, 'slug': 'jaime_lerner_sings_of_the_city', 'viewed_count': 597041}]",
    'Game designer',
    "['cities', 'design', 'future', 'infrastructure', 'play', 'public spaces', 'society', 'software', 'urban planning']",
    'How a video game might help us build better cities',
    'https://www.ted.com/talks/karoliina_korppoo_how_a_video_game_might_help_us_build_better_cities\n',
    '391721']
"""

import csv
import json
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

from operator import itemgetter

from elice_utils import EliceUtils
elice_utils = EliceUtils()


def jsonify(data):
    return json.loads(data.replace("'", '"'))


def preprocess_talks(csv_file):
    # 강연 데이터를 저장할 빈 리스트를 선언합니다.
    talks = []
    
    # CSV 파일을 열고, 데이터를 읽어 와서 talks에 저장합니다.
    with open(csv_file,'r') as cfile:
        reader = csv.reader(cfile)
        
        for row in reader:
            # print(row)
            try:
                talk = {
                    'title': row[14],     # 강연의 제목
                    'speaker': row[6],   # 강연자의 이름
                    'views': int(row[16]),     # 조회수
                    'comments': int(row[0]),  # 댓글의 개수
                    'duration': int(row[2]),  # 강연 길이
                    'languages': int(row[5]), # 지원하는 언어의 수
                    'tags': jsonify(row[13]),      # 관련 태그 (키워드)
                    'ratings': jsonify(row[10]),   # 강의에 대한 평가
                }
            except:
                pass
            talks.append(talk)
    
    return talks


def get_popular_tags(talks, n):
    # 태그 별 인기도를 저장할 딕셔너리
    tag_to_views = {}
    
    # 태그 별 인기도를 구해 tag_to_views에 저장합니다.
    for talk in talks:
        for tag in talk['tags']:
            if tag not in tag_to_views:
                tag_to_views[tag] = 0
            tag_to_views[tag] += talk['views']
    
    # (태그, 인기도)의 리스트 형식으로 변환합니다.
    tag_view_pairs = list(tag_to_views.items())
    
    # 인기도가 높은 순서로 정렬해 앞의 n개를 취합니다.
    # n개를 취한 후에는 태그만 남깁니다.
    # 힌트: itemgetter()를 사용하세요!
    top_tag_and_views = sorted(tag_view_pairs, key=lambda item:item[1], reverse=True)[:n]
    # print('top_tag_and_views',top_tag_and_views)
    top_tags = map(lambda x: x[0] , top_tag_and_views)
    # print('top_tags',list(top_tags))
    return list(top_tags)


def completion_rate_by_duration(talks):
    durations = list(map(lambda x:x['duration'],talks))
    completion_rates = list(map(lambda x: x['comments']/x['views'] , talks))
    # print('durations',list(durations)[:10])
    # print('completion_rates',list(completion_rates)[:10])
    scatter_plot(durations, completion_rates, '강의 길이', '완수도')
    
    return completion_rates, durations


def views_by_languages(talks):
    languages = [ x['languages'] for x in talks ]
    views = [ x['views'] for x in talks ]
    scatter_plot(languages, views, '언어의 수', '조회수')
    
    # 채점을 위해 결과를 리턴합니다.
    return views, languages


def show_ratings(talk):
    
    keywords = [ x['name'] for x in talk['ratings'] ]
    counts = [ x['count'] for x in talk['ratings'] ]
    
    bar_plot(keywords, counts, '키워드', 'rating의 수')
    
    # 채점을 위해 결과를 리턴합니다.
    return keywords, counts


def scatter_plot(x, y, x_label, y_label):
    font = fm.FontProperties(fname='./NanumBarunGothic.ttf')
    
    plt.scatter(x, y)
    plt.xlabel(x_label, fontproperties=font)
    plt.ylabel(y_label, fontproperties=font)
    
    plt.xlim((min(x), max(x)))
    plt.ylim((min(y), max(y)))
    plt.tight_layout()
    
    plot_filename = 'plot.png'
    plt.savefig(plot_filename)
    elice_utils.send_image(plot_filename)


def bar_plot(x_ticks, y, x_label, y_label):
    assert(len(x_ticks) == len(y))
    
    font = fm.FontProperties(fname='./NanumBarunGothic.ttf')
    
    pos = range(len(y))
    plt.bar(pos, y, align='center')
    plt.xticks(pos, x_ticks, rotation='vertical', fontproperties=font)
    
    plt.xlabel(x_label, fontproperties=font)
    plt.ylabel(y_label, fontproperties=font)
    plt.tight_layout()
    
    plot_filename = 'plot.png'
    plt.savefig(plot_filename)
    elice_utils.send_image(plot_filename)


def main():
    src = 'ted.csv'
    talks = preprocess_talks(src)
    print(get_popular_tags(talks, 10))
    completion_rate_by_duration(talks)
    views_by_languages(talks)
    show_ratings(talks[0])


if __name__ == "__main__":
    main()
```

## 최종 시험
- 트윗 분류
```python
def trump_tweet(text) :
    # 주어진 규칙에 맞추어 trump_twit()함수를 구현해주세요.
    # pass는 지우고 코드를 작성해주세요.
    hashList = []
    mentionList = []
    textList = []
    # print(text)
    for t in text.split():
        if t.startswith('@'):
            mentionList.append(t[1:])
        elif t.startswith('#'):
            hashList.append(t[1:])
        else:
            textList.append(t)
    print('hash list :',hashList)
    print('mention list :',mentionList)
    print('text list :',textList)



# 아래 부분은 수정하지 마세요!
# 입력과 출력을 수행하는 코드입니다.
t = input()
trump_tweet(t)
```

- text로 시작하는 상위 20개 출력
```python
def filter_by_text(text) :
    # 주어진 규칙에 맞추어 filter_by_text()함수를 구현해주세요.
    # corpus.txt에 있는 텍스트를 읽어와서 corpus라는 리스트에 추가한다.
    corpus = []
    with open('corpus.txt','r') as file:
        for t in file:
            word , freq = t.split('/')
            corpus.append( (word , int(freq)) )
    
    
    # corpus에 있는 데이터 중, text로 시작하는 단어만을 추려서 result라는 리스트에 저장한다.
    result = [ t for t in corpus if t[0].startswith(text)]
    
    # 찾은 영어 단어를 빈도수를 기준으로 내림차순으로 정렬하여 20개만 출력한다.
    print( sorted(result,key=lambda x: x[1],reverse=True)[:20])
    
    
# 아래 부분은 수정하지 마세요!
# 입력과 출력을 수행하는 코드입니다.
t = input()
filter_by_text(t)
```


