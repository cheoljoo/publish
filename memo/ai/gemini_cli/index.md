- description : Google’s Gemini CLI is INSANE—After 1 Hour of Coding, It’s Still 95% Full! & MCP
- tag : ai, gemini, cli, free , mcp
- date : 2025-06-29

TOC
- [1. 설치 방법](#1-설치-방법)
  - [1.1. 제미나이 CLI 설치 방법](#11-제미나이-cli-설치-방법)
  - [1.2. 제미나이 CLI MCP 설정 방법\*](#12-제미나이-cli-mcp-설정-방법)
  - [1.3. 제미나이 CLI의 프로젝트 지침\*](#13-제미나이-cli의-프로젝트-지침)
- [2. MCP 연결해보기 - youtube](#2-mcp-연결해보기---youtube)
  - [2.1. 그외](#21-그외)
- [3. github 연결하기](#3-github-연결하기)
  - [3.1. private repository 안의 내용을 query](#31-private-repository-안의-내용을-query)
  - [3.2. MCP 사용 - github](#32-mcp-사용---github)
- [4. linux에서 docker를 이용하여 gemini-cli 수행하기](#4-linux에서-docker를-이용하여-gemini-cli-수행하기)
  - [4.1. MCP](#41-mcp)
- [5. In this video you’ll learn:](#5-in-this-video-youll-learn)
- [6. reference](#6-reference)

-------

<H1><p style="color:blue;">Title : ai : Google’s Gemini CLI is INSANE—After 1 Hour of Coding, It’s Still 95% Full! & MCP</p></H1>

- google cli의 사용법을 익혀야 할 것으로 보인다.  아래의 방법을 따라해봐야 한다.
- [youtube](https://www.youtube.com/watch?v=-8Q0wyFaB4M&ab_channel=%EC%86%8C%EC%8A%A4%EB%86%80%EC%9D%B4%ED%84%B0)

# 1. 설치 방법
## 1.1. 제미나이 CLI 설치 방법
- 1단계 : Node 설치하기 (최소 18 버전 이상의 NodeJS가 요구됨)
  - 미설치시 nodejs.org에서 다운로드 & 설치
- 2단계 : 명령프롬프트에서 전역(글로벌) 설치하기 
	- npm install -g @google/gemini-cli
- 3단계 : 작업폴더 위치에서 실행하기
  - gemini           # CLI 시작       (최초로 실행하면 구글 로그인하여 권한 부여가 필요함)
## 1.2. 제미나이 CLI MCP 설정 방법*
- 클로드 데스크톱과 동일합니다.  단 설정 파일이 다른데, C:\사용자\{로컬사용자명}\.gemini\settings.json 이 설정 파일입니다.
- 최초에서 설정 파일 내용이 다음과 같습니다.
  - ```
    {
      "theme": "Default",
      "selectedAuthType": "oauth-personal"
    }

    이것을 다음처럼 바꿉니다.
    {
      "theme": "Default",
      "selectedAuthType": "oauth-personal",
      "mcpServers": {
        이곳에는 클로드 데스크탑의 mcpServers 항목 내용을 그대로 복사해 옵니다. 
      }
    }

    다음은 완성된 설정 내용의 예입니다. (playwright-stealth MCP만 설정된 상태)
    {
      "theme": "Default",
      "selectedAuthType": "oauth-personal",
      "mcpServers": {
        "playwright-stealth": {
          "command": "npx",
          "args": ["-y", "@pvinis/playwright-stealth-mcp-server"]
        }
      }  
    }
    ```
  - 그후 gemini 실행하신 후, /mcp 입력하시면 설치된 MCP들을 볼 수 있습니다.
## 1.3. 제미나이 CLI의 프로젝트 지침*
- gemini 명령어를 실행할 당시의 경로가 작업 폴더, 즉 프로젝트 폴더가 됩니다.
- 이제 gemini는 해당 폴더에 대해서만 파일 생성을 진행합니다.
- 그리고 그 폴더에 GEMINI.md 파일을 생성하시면 해당 파일은 메모리 역할을 하여, 제미나이가 항상 기억합니다.
- 즉 GEMINI.md 파일에 프로젝트 지침을 넣으시면 됩니다.
- 그리고 GEMINI.md 파일을 수정하신 경우, "/memory refresh"를 입력하여 제미나이가 다시 메모리를 읽도록 지시할 수 있습니다.

# 2. MCP 연결해보기 - youtube
- https://lobehub.com/ko/mcp/icraft2170-youtube-data-mcp-server
- YouTube API Setup
  - Access Google Cloud Console
  - Create a new project or select an existing one
  - Enable YouTube Data API v3
  - Create API credentials (API key)
  - Use the generated API key in your environment configuration
- C:\사용자\{로컬사용자명}\.gemini\settings.json 
  - ```json
      {
        "mcpServers": {
          "youtube": {
            "command": "npx",
            "args": ["-y", "youtube-data-mcp-server"],
            "env": {
              "YOUTUBE_API_KEY": "YOUR_API_KEY_HERE",
              "YOUTUBE_TRANSCRIPT_LANG": "ko"
            }
          }
        }
      }
      ```
- npm install youtube-data-mcp-server
- gemini-cli prompt
  - > /mcp
    - ```
      🟢 youtube - Ready (9 tools)
        - getVideoDetails
        - searchVideos
        - getTranscripts
        - getRelatedVideos
        - getChannelStatistics
        - getChannelTopVideos
        - getVideoEngagementRatio
        - getTrendingVideos
        - compareVideos
      ```
  - > 한글로 된 것중에 hot trends인 youtube는 뭐야?
    - ```
      ╭───────────────────────────────────────────────────────────────────────────────────────────────────╮
      │ ✔  getTrendingVideos (youtube MCP Server) {"regionCode":"KR"}                                     │
      │                                                                                                   │
      │    [                                                                                              │
      │      {                                                                                            │
      │        "id": "80qpfeBklWc",                                                                       │
      │        "title": "사회의 쓴맛을 본 사랑이의 눈물💦 오열하는 딸의 모습에 같이 울컥한 야노 시호      │
      │    #내아이의사생활 EP.27",                                                                        │
      │        "channelTitle": "ENA 이엔에이",                                                            │
      │        "publishedAt": "2025-06-29T12:22:01Z",                                                     │
      │        "viewCount": "1476791",                                                                    │
      │        "likeCount": "11159"                                                                       │
      │      },                                                                                           │
      │    ]                                                                                              │
      ╰───────────────────────────────────────────────────────────────────────────────────────────────────╯
      ✦ 한국에서 현재 인기 있는 YouTube 동영상은 다음과 같습니다:
        * 사회의 쓴맛을 본 사랑이의 눈물💦 오열하는 딸의 모습에 같이 울컥한 야노 시호 #내아이의사생활 EP.27 (ENA
          이엔에이 채널) - 조회수 1,476,791회
        * [UFC] 일리아 토푸리아 vs 찰스 올리베이라 (tvN SPORTS 채널) - 조회수 1,321,989회
      ```
- mcp set하지 않았을때 prompt 결과
  - > Youtube에서 hot trends가 되는 ko 기반의 contents 5개만 추천해줘?
    - ```
      ╭───────────────────────────────────────────────────────────────────────────────────────────────────╮
      │ ✔  GoogleSearch Searching the web for: "YouTube hot trends Korean content recommendations"        │
      │                                                                                                   │
      │    Error performing web search.                                                                   │
      ╰───────────────────────────────────────────────────────────────────────────────────────────────────╯
      ✦ 죄송합니다. 현재 웹 검색 기능에 문제가 발생하여 YouTube의 인기 한국 콘텐츠를 추천해 드릴 수 없습니다.
      ```

## 2.1. 그외
- C:\사용자\{로컬사용자명}\.gemini\settings.json 의 mcpServers에 playwright를 설정
  - ```json
    "mcpServers": {
      "playwright-stealth": {
        "command": "npx",
        "args": [
          "-y",
          "@pvinis/playwright-stealth-mcp-server"
        ]
      }
    ```
  - github token생성 참조 [url](https://sprint.codeit.kr/blog/github%EC%97%90%EC%84%9C-%ED%86%A0%ED%81%B0-%EB%B0%9C%EA%B8%89%ED%95%98%EA%B8%B0)
  - token은 생성되었을때만 보이므로 잘 적어두어야 한다.
  - "investing.com 에서 삼성전자의 10년치 배당금을 찾아줘". 라고 하면 뭔가 mcp의 playwright로 연결하여 agent를 수행하다 잘 안되는 모습이 보임
  - [@modelcontextprotocol/server-filesystem](https://www.npmjs.com/package/@modelcontextprotocol/server-filesystem) 을 사용하여 보려고 했지만,  docker로 뭔가 하면 될 듯 한데 , docker를 사용하지 않고는 잘 안된다.
    - 그냥 c:\code안의 내용을 보고 싶으면 cd c:\code ; gemini를 하는 방법과
    - 특별히 보고 싶은 것을 git clone 해 달라고 한 후에 gemini를 수행시킨 아래에 git clone이 되게 되고 이 정보를 이용하여 query를 할수 있다.

# 3. github 연결하기
## 3.1. private repository 안의 내용을 query
  - > git clone https://github.com/cheoljoo/memo 을 하여 download 한 후에 이 내용을 본다. 
  - 결과
    - ```
      > git clone https://github.com/cheoljoo/memo
      > memo git을 git pull 한 후에 못 이 들어 있는 box를 알려주세요
      ✦ Git pull이 완료되었습니다. 이제 "못"이 들어있는 박스를 찾아보겠습니다.
      ╭────────────────────────────────────────────────────────╮
      │ ✔  ReadFile ...memo\label\img\label-box-in-my-room.md  │
      ╰────────────────────────────────────────────────────────╯
      ✦ "못"이 들어있는 박스는 Box 8 입니다.
      ```
  - github의 MCP은 private repository는 지원하지 않음.
## 3.2. MCP 사용 - github
- [github token 생성](https://sprint.codeit.kr/blog/github%EC%97%90%EC%84%9C-%ED%86%A0%ED%81%B0-%EB%B0%9C%EA%B8%89%ED%95%98%EA%B8%B0)
- C:\사용자\{로컬사용자명}\.gemini\settings.json 
  - ```json
      {
        "mcpServers": {
          "github": {
            "command": "npx",
            "args": [
              "-y",
              "@modelcontextprotocol/server-github"
            ],
            "env": {
              "GITHUB_TOKEN": "your_key"
            }
          }
        }
      }
      ```
- npm install -g @modelcontextprotocol/server-github
- gemini-cli prompt
  - > /mcp
    - ```
      🟢 github - Ready (26 tools)
        - create_or_update_file
        - search_repositories
        - create_repository
        - get_file_contents
        - push_files
        - create_issue
        - create_pull_request
        - fork_repository
        - create_branch
        - list_commits
        - list_issues
        - update_issue
        - add_issue_comment
        - search_code
        - search_issues
        - search_users
        - get_issue
        - get_pull_request
        - list_pull_requests
        - create_pull_request_review
        - merge_pull_request
        - get_pull_request_files
        - get_pull_request_status
        - update_pull_request_branch
        - get_pull_request_comments
        - get_pull_request_reviews
      ```
  - > github의 cheoljoo 안에 있는 repositories는 무엇이 있는가?
    - ```
      ╭───────────────────────────────────────────────────────────────────────────────────────────────────╮
      │ ✔  search_repositories (github MCP Server) {"query":"user:cheoljoo"}                              │
      │                                                                                                   │
      │    ... first 709 lines hidden ...                                                                 │
      │          "id": 254219808,                                                                         │
      │          "node_id": "MDEwOlJlcG9zaXRvcnkyNTQyMTk4MDg=",                                           │
      │          "name": "dart",                                                                          │
      │          "full_name": "cheoljoo/dart",                                                            │
      │          "private": false,                                                                        │
      │          "owner": {                                                                               │
      │            "login": "cheoljoo",                                                                   │
      │            "id": 5361719,                                                                         │
      │            "node_id": "MDQ6VXNlcjUzNjE3MTk=",                                                     │
      │            "avatar_url": "https://avatars.githubusercontent.com/u/5361719?v=4",                   │
      │            "url": "https://api.github.com/users/cheoljoo",                                        │
      │            "html_url": "https://github.com/cheoljoo",                                             │
      │            "type": "User"                                                                         │
      │          },                                                                                       │
      │          "html_url": "https://github.com/cheoljoo/dart",                                          │
      │          "description": null,                                                                     │
      │          "fork": false,                                                                           │
      │          "url": "https://api.github.com/repos/cheoljoo/dart",                                     │
      │          "created_at": "2020-04-08T23:02:08Z",                                                    │
      │          "updated_at": "2020-04-14T12:51:24Z",                                                    │
      │          "pushed_at": "2020-04-14T12:51:22Z",                                                     │
      │          "git_url": "git://github.com/cheoljoo/dart.git",                                         │
      │          "ssh_url": "git@github.com:cheoljoo/dart.git",                                           │
      │          "clone_url": "https://github.com/cheoljoo/dart.git",                                     │
      │          "default_branch": "master"                                                               │
      │        },                                                                                         │
      ╰───────────────────────────────────────────────────────────────────────────────────────────────────╯
      ✦ cheoljoo님의 GitHub에는 총 33개의 repository가 있으며, 그중 일부는 다음과 같습니다.
        * educated-advanced-cpp: C++ Idioms & Advanced C++
        * doxygen_perlmod_python: doxygen에서 GENERATE_PERLMOD를 설정할 때 더 많은 파이썬 예제와 사용법을 제공합니다.
        * CGA_AGP: 프로토콜용 파서 자동 생성기
        * fish: FISH (Funny sImple distributed system with rSH through sSH)
        * weekly_report_4_jira: <wr> 형식에 대한 jira 및 댓글 분석을 통한 주간 보고서
        * schedule: 나의 일정 및 할 일 목록
        * cheoljoo.github.io: charles 블로그 (cheoljoo@gmail.com)
        * problemSolving: 문제 해결
        * doxygen_aspice: 모든 파이썬 개발자를 위한 ASPICE 문서 생성기
        * dltString: DLT_LOG 문자열 크기 줄이기
        * ps_ai: 문제 해결 및 AI 정보
        * System_Trading: 시스템 트레이딩
        * publish: 게시
        * test-dynamic-so: 동적 so 테스트 - 사용 바이너리와 재컴파일 간의 멤버 함수 순서 변경
        * educated-functional-programming-haskell: 함수형 프로그래밍 - 하스켈
        * educated-templateMetaProgramming: 템플릿 메타 프로그래밍
        * educated-cpp-STL-Programming: C++ STL 프로그래밍
        * processMap: 상태 확인 결과와 함께 프로세스 맵을 위한 plantuml
        * educated-html5-css5-newbie: HTML5 및 CSS5 초보자 교육
        * educated-bigDataWithR: R을 이용한 빅데이터 연구
        * python-learn: 파이썬 학습
        * supergoop-crawler: supergoop 크롤러
        * stock_samsung: 삼성전자와 삼성전자(우)의 비교 : 언제 어떤 것을 사야 유리한지?
        * educated-dataAnalysis_Visualization: 데이터 분석 및 시각화 교육
        * educated-basic-cpp: C++ 기초 교육
        * educated-gtest: gtest 교육
        * dart: 다트
        * mouse_ocr_editor: ocr 결과(easyocr)를 기반으로 포인트와 사각형을 쉽게 편집할 수 있는 편집기
        * educated-unittest-intermediate: 유닛테스트 중급 교육
        * nm: nm c++filt
        * educated-advanced-cpp: C++ Idioms & Advanced C++
        * doxygen_perlmod_python: doxygen에서 GENERATE_PERLMOD를 설정할 때 더 많은 파이썬 예제와 사용법을 제공합니다.
        * CGA_AGP: 프로토콜용 파서 자동 생성기
        * fish: FISH (Funny sImple distributed system with rSH through sSH)
        * weekly_report_4_jira: <wr> 형식에 대한 jira 및 댓글 분석을 통한 주간 보고서
        * schedule: 나의 일정 및 할 일 목록
        * cheoljoo.github.io: charles 블로그 (cheoljoo@gmail.com)
        * problemSolving: 문제 해결
        * doxygen_aspice: 모든 파이썬 개발자를 위한 ASPICE 문서 생성기
      ```

# 4. [linux에서 docker를 이용하여 gemini-cli 수행하기](https://github.com/cheoljoo/gemini-cli-docker)
- Google AI Studio API 키를 얻으려면 Google AI Studio 웹사이트(aistudio.google.com)에서 API 키 페이지로 이동하여 API 키를 생성하고 복사해야 합니다. 
  - Google AI Studio 접속: Google AI Studio 웹사이트에 접속합니다. 
  - API 키 페이지 이동: 왼쪽 탐색 메뉴에서 "Get API Key"를 클릭하거나, API 키 페이지로 직접 이동합니다. 
  - API 키 생성: 제공된 지침에 따라 API 키를 생성합니다. 
  - API 키 복사: 생성된 API 키를 복사하여 안전한 곳에 보관합니다. 
- Dockerfile
    - ```
      # Use the latest LTS version of Node.js as the base image
      FROM node:lts-slim

      # 베이스 이미지로 Node.js를 사용합니다.
      #FROM node:latest

      # 작업 디렉토리를 설정합니다.
      WORKDIR /usr/src/app

      # 글로벌로 gemini-cli를 설치합니다.
      RUN npm install -g @google/gemini-cli

      # 환경 변수를 설정합니다.
      ENV GEMINI_API_KEY=[your_gemini_api_key]

      # 현재 호스트의 사용자 ID와 그룹 ID를 환경 변수로 전달합니다.
      ARG USER_ID
      ARG GROUP_ID

      # 사용자와 그룹을 생성합니다.
      RUN groupadd -g ${GROUP_ID} appgroup && \
          useradd -u ${USER_ID} -g appgroup -m appuser

      # 생성한 사용자로 실행되도록 설정합니다.
      USER appuser

      # 컨테이너가 시작될 때 실행할 명령을 설정합니다.
      CMD ["gemini", "-y"]
      ```
    - edit [your_gemini_api_key]
- git clone http://mod.lge.com/hub/cheoljoo.lee/misc.git
    - cd misc/gemini-cli
    - make build
      - ```docker build --build-arg USER_ID=`id -u` --build-arg GROUP_ID=`id -g` -t gemini-app .```
    - make
      - ```docker run -it --rm --name gemini-container2 -v ./:/usr/src/app  -e GEMINI_API_KEY=[your-gemini-api-key] gemini-app```
- prompt
  - ```
    > - 설치가 필요시 sudo 를 이용하여 설치해줘
      - samsung_ltd_price.json : 삼성전자의 2015년 1월 1일 부터의 일별 시작가 , 종가 확보
      - dictionary type으로 만들어주세요. { 'YY-mm-dd' : 'open': 시작가격 , 'close': 종가 }
      - 정보를 획득하는 python code를 만들고 저장해주며 , 이를 수행하여 samsung_ltd_price.json 결과도 저장을 해주십시요.
    ```
- 여기서는 -y 로 수행했기에 여러가지를 설치를 자동으로 하고 수행하여 , 수행한 directory에 get_samsung_stock_price.py  samsung_ltd_price.json을 생성시켜준다.
## 4.1. MCP
  - .gemini/settings.json
    - ```json
      {
            "theme": "Default",
            "selectedAuthType": "gemini-api-key",
            "mcpServers": {
              "playwright-stealth": {
                "command": "npx",
                "args": ["-y", "@pvinis/playwright-stealth-mcp-server"]
              },
              "youtube": {
                  "command": "npx",
                  "args": ["-y", "youtube-data-mcp-server"],
                  "env": {
                    "YOUTUBE_API_KEY": "[your-api-key]",
                    "YOUTUBE_TRANSCRIPT_LANG": "ko"
                  }
              },
              "github": {
                  "command": "npx",
                  "args": [
                    "-y",
                    "@modelcontextprotocol/server-github"
                  ],
                  "env": {
                    "GITHUB_TOKEN": "[your-api-key]"
                  }
              }
            }
      }
      ```
    - 수행할 곳에 ```mkdir .gemini``` 한 후에 ```vi .gemini/settings.json```으로 위의 내용을 넣어주세요.
  - 수행 결과
    - ```
      > youtube 의 한국내 top3 trend를 URL과 같이 보여주세요

      ╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
      │ ✔  getTrendingVideos (youtube MCP Server) {"regionCode":"KR","maxResults":3}                                                                                                                                                        │
      │    [                                                                                                                                                                                                                                │
      │      {                                                                                                                                                                                                                              │
      │        "id": "80qpfeBklWc",                                                                                                                                                                                                         │
      │        "title": "[SUB] 사회의 쓴맛을 본 사랑이의 눈물💦 오열하는 딸의 모습에 같이 울컥한 야노 시호 #내아이의사생활 EP.27",                                                                                                          │
      │        "channelTitle": "ENA 이엔에이",                                                                                                                                                                                              │
      │        "publishedAt": "2025-06-29T12:22:01Z",                                                                                                                                                                                       │
      │        "viewCount": "3223687",                                                                                                                                                                                                      │
      │        "likeCount": "21641"                                                                                                                                                                                                         │
      │      },                                                                                                                                                                                                                             │
      │      {                                                                                                                                                                                                                              │
      │        "id": "EbxCy2GEPIs",                                                                                                                                                                                                         │
      │        "title": "윤형빈 (YOON HYUNG-BIN) vs 밴쯔 (BANZZ) [FULL FIGHT] [굽네 ROAD FC 073]",                                                                                                                                          │
      │        "channelTitle": "ROAD FIGHTING CHAMPIONSHIP",                                                                                                                                                                                │
      │        "publishedAt": "2025-06-28T12:28:18Z",                                                                                                                                                                                       │
      │        "viewCount": "1484628",                                                                                                                                                                                                      │
      │        "likeCount": "7610"                                                                                                                                                                                                          │
      │      },                                                                                                                                                                                                                             │
      │      {                                                                                                                                                                                                                              │
      │        "id": "katO8j29gJw",                                                                                                                                                                                                         │
      │        "title": "ALLDAY PROJECT - FAMOUS | SBS 250629 방송",                                                                                                                                                                        │
      │        "channelTitle": "SBSKPOP X INKIGAYO",                                                                                                                                                                                        │
      │        "publishedAt": "2025-06-29T07:03:04Z",                                                                                                                                                                                       │
      │        "viewCount": "1128121",                                                                                                                                                                                                      │
      │        "likeCount": "46297"                                                                                                                                                                                                         │
      │      }                                                                                                                                                                                                                              │
      │    ]                                                                                                                                                                                                                                │
      ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
      ✦ 한국 유튜브 트렌드 Top 3:
        1. [SUB] 사회의 쓴맛을 본 사랑이의 눈물💦 오열하는 딸의 모습에 같이 울컥한 야노 시호 #내아이의사생활 EP.27: https://www.youtube.com/watch?v=80qpfeBklWc
        2. 윤형빈 (YOON HYUNG-BIN) vs 밴쯔 (BANZZ) [FULL FIGHT] [굽네 ROAD FC 073]: https://www.youtube.com/watch?v=EbxCy2GEPIs
        3. ALLDAY PROJECT - FAMOUS | SBS 250629 방송: https://www.youtube.com/watch?v=katO8j29gJw

      Using 3 MCP servers (ctrl+t to view)                                     
      ```

# 5. In this video you’ll learn:
- [youtube](https://www.youtube.com/watch?v=-8Q0wyFaB4M&ab_channel=%EC%86%8C%EC%8A%A4%EB%86%80%EC%9D%B4%ED%84%B0)
- Gemini CLI Quick-Start
  - Get up and running in minutes.
- Project & Memory Management
  - The current working directory is auto-set as your “workspace.” See how to inspect and refresh memory on the fly.
- MCP Integration Tips
  - Copy your Claude Desktop MCP config straight into .gemini/settings.json and reuse it instantly.
- Hands-On Demo
  - Launch a browser with MCP and run Playwright-based automated tests.
- Gemini CLI Pros & Cons
  - Huge context window (95 % tokens free) and zero cost are major perks, but early-release bugs still pop up.
- Efficient AI-Coding Tactics
  - Build a logging system, keep MVC separation, use “deep questioning” for better debugging, and break big tasks into smaller loops for rock-solid reliability.

# 6. reference
- [Gemini CLI와 프롬프트 래핑(Wrapping)으로 자동화 프롬프트 활용하기](https://adjh54.tistory.com/700#5.%20%ED%84%B0%EB%AF%B8%EB%84%90%EC%97%90%EC%84%9C%20Gemini%20CLI%EB%A5%BC%20%EC%8B%A4%ED%96%89%ED%95%A9%EB%8B%88%EB%8B%A4-1-13)
  - https://github.com/cheoljoo/english.git