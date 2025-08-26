- description : english conversation with AI
- tag : ai, english, conversation
- date : 2025-08-04

-------


<H1><p style="color:blue;">Title : english conversation with AI</p></H1>

# 목적
- 차에서나 산책시 영어 회화를 음성으로 할수 있는 방법을 찾자.
  - 차에서 사용하는 것은 가능하면 음성으로만 모든 것이 가능했으면 한다.
  - 산책시는 필요하면 버튼을 누르며 대화 가능하다.
- 비용 절약 : 이 부분이 잘되면 영어 회화 비용을 최대한으로 줄일수 있다.
- 

# 시도하는 것
## gemini
- GEM : 영어 중급 회화 사용중 2025-08-04 13:49:27

## gemini-cli
- git clone https://github.com/cheoljoo/english.git
- cd english
- gemini-cli 수행
  - ```prompt
    database.csv 은 csv 형식의 파일이며 ,
      - date : 날짜
      - URL : 기사 URL
      - topic : 기사 제목
    을 가지고 있다. 
    
    contents.json 이라는 파일을 읽어서, URL이 이미 포함된 것은 skip한다.
    새로운 URL인 경우에는 다음의 내용을 읽어와서 새로운 파일에 다음과 같이 결과를 json 형식으로 contents.json에 모두 영어로 기록해주었으면 한다.
      - date : 위의 날짜
      - topic : 기사 제목
      - URL : 기사 URL
      - source : URL있는 기사의 Text 부분만 발췌 (광고등은 제거하고 기사 부분만을 발췌해달라.)
      - summary : 기사 내용을 summary해 달라. 최대 400자 이내로 summary해 달라. 
    ```

# 여러가지 실패한 시도들 (실패)
## gemini
- GEM 사용 : 2025-08-04 13:49:15
  - 사유
    - 내부에서 다시 내부의 link를 불러 달라고 하면 에러가 발생함.
  - 대책
    - cheoljoo.github.io에 내용들을 요약해서 바로 넣어두는 것을 만들어두면 가능할 듯하다.
  - 내용
    - ```txt
      https://raw.githubusercontent.com/cheoljoo/english/refs/heads/main/database.csv
      의 정보를 보고 오늘 날짜에 해당하는 [URL] [topic] 을 보고 [URL]에 접속하여 내용을 요약해 달라. 
      이후 우리는 영어로 서로 대화를 할 것이다.

      너는 질문자가 되고 , 
      나는 답변하는 자가 될 것이다. 
      만약 내가 질문을 하게 괴면 너는 답변을 해주면 된다.

      내가 답변자 일때는 나의 영어를 한 번 반복해주고,
      이를 더 좋은 영어 표현으로 고쳐달라. 

      이후 

      한글로 마무리를 해달라고 하면
      영어로 전체 내용을 요약해주고,
      이중에서 중요한 영어 표현들 5개를 뽑아서 https://docs.google.com/spreadsheets/d/1Qle98To82Wte2THzsPwVVspnEPFdEwbCj-xwjF5OB1U/edit?gid=0#gid=0 안의 
      [DATE] [ENGLISH] [KOREAN] [URL] 에 계속 추가해주었으면 해
      [DATE]는 오늘 날짜
      [URL]은 해당 대화를 다시 볼수 있는 URL
      [ENLISH]는 위의 중요한 5개의 영어 표현
      [KOREAN]은 [ENGLISH]에 대한 한국어 표현
      ```

# ideation
- 일을 잘게 나누어야 한다. 
- prompt로 시킬 것을 명확하게 세분화를 해야 한다.
- 예
  - 기사를 RSS를 이용해서 가져오는 것은 python으로 만든다. (news_collector.py)
  - 이를 요약해주는 기능만을 LLM에 맡긴다.
  - 가져오고 요약한 내용을 merge.py를 이용하여, database.csv와 contents.json 에 합치는 작업을 한다. (merge.py)
  - contents.json을 바로 cheoljoo.github.io에서 볼수 있게 html로 변환을 한다. (json_to_html.py)
- 주의 사항:
  - LLM에 문의할때 URL이 있으면 그것에 접속하며 뭔가를 시도하려한다.
  - chatgpt와 gemini가 다르다.
    - 각각에서 수행을 시켜보고 더 적합한 것을 찾으면 좋을 듯!   
      - chatgpt의 경우 prompt를 따로 입력할 필요없이 어디에 등록가능하게도 만들어줄수 있다.   
      - gmini에서도 gem 에 넣어서 사용해보는게 좋을 듯!


!!!!다시 정리 필요!!!!
- 내일 동작이 잘되는지 먼저 봐야 할 듯.
- 최신 10개의 내용중에서 찾아서 서로 대화를 할수 있는지 test 필요
- free account에서도 되는지 살펴볼 것