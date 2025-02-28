# - description : memo subdirectories가 다루는 내용들을 network graph map 으로 보여준다.
# - tag : python , run , json , network-graph , html


comments_prompt = """file_to_tag_dict =  {'./git_console_analysis.md': {'description': 'git blame을 다루는 법', 'tag': ['git', 'blame']}, './ai-Google-NotebookLM-vs-GPTs.md': {'description': 'google notebooklm과 openai chatgpt를 비교해 놓은 페이지이다.', 'tag': ['ai', 'chatgpt', 'notebooklm', 'openai', 'google']}, './lge-works.md': {'description': '2025 year LGE work history', 'tag': ['2025', 'lge', 'work', 'history']}, './future.md': {'description': '앞으로 어떤 방향성을 가지고 내가 살아가야 할지 의견을 적어두는 것이다. 가끔 좋은 책 / 글 / 동영상을 보고 생각나는 부분들을 적어두는 것이다.', 'tag': ['future', 'my-life', 'life', 'direction']}, './log.md': {'description': 'log을 어ㄸ허게 잘 작성할수 있을까? 및 log framework 조사', 'tag': ['log', 'python', 'meta-calss', 'decorator', 'bash']}, './toc.md': {'description': 'log을 어ㄸ허게 잘 작성할수 있을까? 및 log framework 조사', 'tag': ['log', 'python', 'meta-calss', 'decorator', 'bash']}, './ai-education.md': {'description': 'AI 교육 list를 모아둔 것이다. 꼭 들어야 하는데 잘 안되어 아쉽다.', 'tag': ['ai', 'education']}, './AI-study.md': {'description': 'ai에 대한 교육 내용을 적어둔 것이다. 일단 김진형 / 김인중 교수님의 내용에 대해서 들은 것을 정리해두었다.', 'tag': ['ai', 'study', '김진형', '김인중', 'machine-learning']}, './dreamhack.md': {'description': 'dreamhack (LGE 해킹대회 사전 교육) 관련 정리하던 것으로 , 제대로 끝내지 못한 교육이었음.', 'tag': ['dreamhack', 'education']}, './github_recovery_code.md': {'description': 'github 관련 private 정보들', 'tag': ['girhub', 'private']}, './linux_shell_script.md': {'description': 'bash scripts 모음', 'tag': ['bash', 'scripts']}, './tax.md': {'description': '세금 (tax) 관련 정리', 'tag': ['tax']}, './xml-parse.md': {'description': 'xml parsing 하는 내용 정리', 'tag': ['doxygen', 'xml', 'parsing']}, './comments.md': {'description': 'clean code의 주석부분으로 어떻게 주석을 잘 쓸 것인지? 주석을 문서화 시키는 부분', 'tag': ['clean-code', 'comments', 'docstring', '']}, './lge-2022.md': {'description': '2022 year LGE work history', 'tag': ['2022', 'lge', 'work', 'history']}, './lge-2021.md': {'description': '2021 year LGE work history', 'tag': ['2021', 'lge', 'work', 'history']}, './binary_data_int_console_system_popen.md': {'description': 'python에서 Popen (process run)을 사용할때의 주의점', 'tag': ['python', 'Popen', 'subprocess']}, './airflow.md': {'description': 'airflow 관련 내용을 정리해두는 페이지이다.', 'tag': ['airflow', 'etl']}, './recruit.md': {'description': 'recruit 관련 글 모음 - 이력서 작성도 연관됨.', 'tag': ['recruit', 'resume', 'future', 'life']}, './diary-for-work.md': {'description': '매일 쓰는 일에 대한 일기 - work diary (Routine , Completed , Work In Progress , Next Steps , Learning , Challenges)', 'tag': ['diary', 'work', '']}, './memo-2022-2023.md': {'description': '2022~2023 year 메모 모음', 'tag': ['2022', '2023', 'memo']}, './get-all-description-and-tag.py': {'description': 'education 관련 csv내용을 markdown으로 변환하는 프로그램', 'tag': ['education', 'python', 'run', 'csv', 'markdown', 'convert']}, './mouse.md': {'description': 'JIRA / CodeBeamer / Gerrit등의 개발 시스템을 사용하는 사용자들의 performance가 어떻게 되는지를 check하기 위한 project (MOUSE)', 'tag': ['mouse', 'performance', 'check']}, './aloga.md': {'description': 'ALOGA project에 대한 설명을 달아둔 것으로 , log (DLT)를 분석하여 matching되는 text , scenario가 제대로 나오는지를 판단해주는 project에 대한 설명이다.', 'tag': ['aloga', 'python', 'docker']}, './memory-release-RAII.md': {'description': 'C++ automatic memory management (protect memroy leak) - made by chatgpt', 'tag': ['c++', 'memory', 'leak', 'RAII']}, './openai_chatgpt.md': {'description': 'openai chatGPT에 대한 글 (out-of-date)', 'tag': ['openai', 'chatgpt']}, './vbee_for_tiger4.0.md': {'description': 'vbee', 'tag': ['vbee', 'tcmd']}, './chart.js.md': {'description': '개발시 많이 필요한 chart에 대한정보를 가지고 있다.', 'tag': ['chart.js', 'google-chart', 'mixed']}, './getting_started_tidl_document_2024Y.md': {'description': 'TIDL (Tiger Interface Definition Language)을 수행시키는 starting part만 적어둔 것이다.', 'tag': ['TIDL', 'docker']}, './convert_csv_to_md.sh': {'description': 'csv를 md로 변환시켜주는 convert bash로써 여기서는 실제로 각 directory에 맞는 convert_csv_to_md*.py 를 수행하는 script이다.', 'tag': ['csv', 'md', 'convert']}, './ai.elice.io_파이썬 데이터 분석 기초.md': {'description': 'ai 관련 교육 내용중 내가 모르던 것을 요약했다.  교육명 : 파이썬 데이터 분석 기초', 'tag': ['ai', 'elice.io', 'python', 'data', 'analysis']}, './쿠버네티스_입문(책_요약).md': {'description': '쿠버네티스 () 정리 : 미진 (보다가 중단함)', 'tag': ['book', '쿠버네티스', 'kubernetes', 'devops']}, './git.md': {'description': 'git contribution 방법 / git repository 옮기기 / push commit 변경 등 git 관련 사항 들 정리', 'tag': ['git', 'github']}, './clean-code.md': {'description': 'clean code에 대해서 한글로 정리한 것을 나에 맞게 다시 요약한 것이다.', 'tag': ['clean', 'code', 'clean-code']}, './duplication-check-result.md': {'description': 'TIGER 사용 프로젝트에서 sldd밑에 expected*.csv , auto_test*.csv가 존재하게 되는데, 이때 중복이 발생하면 안된다. 이에 대해서 조사를 하고 문제점이 무엇인지를 정리한 페이지이다.', 'tag': ['lge', 'work', 'duplication', 'check', 'aloga', 'TAF', 'automation']}, './todo.md': {'description': '2025 year TODO 모음', 'tag': ['2025', 'todo']}, './getting_started_tcmd_fish_cisco.md': {'description': 'cisco style command line interface에 대한 정보이다. fish project에 구현이 되어져있고, 상세 설명도 잘 되어져있다. C++ version도 구현되어져있다.', 'tag': ['c++', 'python', 'cisco', 'cli']}, './toto-2024.md': {'description': '2024 year TODO', 'tag': ['2024', 'todo']}, './2023-CDP.md': {'description': '2023 year LGE CDP', 'tag': ['2023', 'lge', 'work', 'CDP']}, './english.md': {'description': 'somedaytalk 영어를 준비하기 위한 페이지로써 영어 공부를 하기 위한 페이지이다. 주로 article을 읽고 나의 summary를 한 후에 이에 대한 수정을 chatGPT에 맡긴 내용을 담고 있다.', 'tag': ['english', 'somedaytalk', '']}, './tcmd.md': {'description': 'tcmd (tiger command)에 대한 실행 및 unittest 방법', 'tag': ['tcmd', 'run', 'unittest']}, './ai-replit-analysis-for-runOnSave.md': {'description': 'runOnSave라는 vscode extension에 대한 분석을 replit에 맡긴 결과를 적어놓은 것이다.', 'tag': ['vscode', 'runOnSave', 'ai', 'extension']}, './vscode.md': {'description': 'vscode 관련 나의 정리', 'tag': ['vscode', 'shortkey']}, './memo-2024.md': {'description': '2024 year 메모 모음', 'tag': ['2024', 'memo']}, './kill_waitpid.md': {'description': 'C / C++ 코드에서    fork 한  process 를  pid 으로  kill 할 때   자식 process 까지  다 죽도록 만들려면,어떻게 할 수 있을까요?', 'tag': ['c', 'c++', 'waitpid', 'zombie']}, './getting_started_doxygen_2024Y.md': {'description': 'doxygen 관련 내가 한 내용들을 정리한 것이다. 여기에 추가하여 doxygen의 internal document를 만들어 ebook으로 만들기를 원한다.', 'tag': ['doxygen', 'ebook', 'code-analysis', '']}, './data-science.md': {'description': 'data science에 대해서 추천 책 / 글들을 모아둔 페이지를 그대로 copy해둔 것이다. origin을 참조하기 바란다.', 'tag': ['DE', 'data', 'engineer', 'data-science', 'recommendation', '']}, './lge-2023.md': {'description': '2023 year LGE work history', 'tag': ['2023', 'lge', 'work', 'history']}, './autohotkey_mini_keyboard.md': {'description': '구매한 autohotkey와 mini keyboard의 사용 조합에 대한 페이지이다.', 'tag': ['autohotkey', 'mini-keyboard']}, './ai-robot.md': {'description': '로봇 관련 글들을 모아놓은 것이다. 로봇에 대한 설명과 요즘의 추세를 적어둔 페이지이다.', 'tag': ['ai', 'robot']}, './stock.md': {'description': '주식 관련', 'tag': ['stock']}, './how_to_write_memo.md': {'description': 'memo 작성법', 'tag': ['memo', 'writing']}, './book/book.md': {'description': '읽어야할 책 리스트', 'tag': ['book', 'list', 'reading', 'future']}, './book/book-review.md': {'description': '(book정리) book review한 것으로 directory가 필요하지 않은 것들을 한번에 모아둔 페이지이다.', 'tag': ['book', 'summary', 'my-summary', 'DE', 'data-science', 'bigData']}, './book/convert_csv_to_md-for-book.py': {'description': 'book 관련 csv내용을 markdown으로 변환하는 프로그램', 'tag': ['book', 'python', 'run', 'csv', 'markdown', 'convert']}, './book/index.md': {'description': 'book review : 읽은 책 내용 정리', 'tag': ['book', 'list']}, './book/fundamentals-of-data-engineering/index.md': {'description': '(book정리) Fundamentals of data engineering - DE', 'tag': ['book', 'summary', 'my-summary', 'DE', 'data-science']}, './book/python-pandas-금융-데이터-분석을-위한/index.md': {'description': '(book정리) 금융 데이터 분석을 위한 파이썬 판다스', 'tag': ['book', 'summary', 'my-summary', 'DE', 'data-science', 'python', 'pandas']}, './book/대규모-데이터!-세트를-위한-알고리즘과-데이터-구조/boyer-more-majority-vote.py': {'description': '(book정리) 금융 데이터 분석을 위한 파이썬 판다스', 'tag': ['book', 'summary', 'my-summary', 'DE', 'data-science', 'python', 'pandas']}, './book/대규모-데이터!-세트를-위한-알고리즘과-데이터-구조/index.md': {'description': '(book정리) algorithms-and-data-structures-for-massive-datasets (대규모-데이터!-세트를-위한-알고리즘과-데이터-구조)', 'tag': ['book', 'summary', 'my-summary', 'DE', 'data-science', 'bigData']}, './book/알고리즘-문제해결전략/알고리즘-문제해결전략.md': {'description': '(book정리) 알고리즘 문제해결 전략에 소개되는 문제해결 방법 (임효준 위원님 추천책)', 'tag': ['book', 'summary', 'my-summary', 'algorithm', 'problem', 'solving']}, './education/convert_csv_to_md-for-education.py': {'description': 'education 관련 csv내용을 markdown으로 변환하는 프로그램', 'tag': ['education', 'python', 'run', 'csv', 'markdown', 'convert']}, './education/index.md': {'description': 'education review : 교육 받은 내용 정리', 'tag': ['education', 'list']}, './education/손에-잡히는-소프트웨어-아키텍처-설계_Python/index.md': {'description': '(education정리) 손에-잡히는-소프트웨어-아키텍처-설계_Python', 'tag': ['education', 'summary', 'my-summary', 'python', 'design', 'pattern', 'architecture']}, './education/업무-효율을-확-끌어올리는-GitHub-Copilot활용-프로그래밍/index.md': {'description': '(education정리) AI 업무-효율을-확-끌어올리는-GitHub-Copilot활용-프로그래밍', 'tag': ['education', 'summary', 'my-summary', 'ai', 'github', 'copilot']}, './education/업무-효율을-확-끌어올리는-MS365-Copilot-프롬프트-마스터-클래스/index.md': {'description': '(education정리) AI 업무-효율을-확-끌어올리는-MS365-Copilot-프롬프트-마스터-클래스', 'tag': ['education', 'summary', 'my-summary', 'ai', 'ms365', 'copilot', 'prompt']}, './education/업무-효율을-확-끌어올리는-LangChain과-함께하는-LLM-기반-애플리케이션-개발/index.md': {'description': '(education정리) AI 업무-효율을-확-끌어올리는-LangChain과-함께하는-LLM-기반-애플리케이션-개발', 'tag': ['education', 'summary', 'my-summary', 'ai', 'langchain', 'LLM']}, './youtube/convert_csv_to_md-youtube.py': {'description': 'youtube 시청한 csv내용을 markdown으로 변환하는 프로그램', 'tag': ['youtube', 'python', 'run', 'csv', 'markdown', 'convert']}, './youtube/index.md': {'description': 'youtube review : Youtube 동영상 시청한 내용 정리', 'tag': ['youtube', 'list']}, './youtube/챗GPT로-미국-주식-포트폴리오-자동으로-관리하는-방법-feat-구글-스프레드-시트-Apps-Script-코드-작성/readme.md': {'description': '(youtube정리) 챗GPT로 미국 주식 포트폴리오 자동으로 관리하는 방법 feat 구글 스프레드 시트, Apps Script 코드 작성', 'tag': ['youtube', 'summary', 'my-summary', 'visualization', 'apps', 'scripts', 'goodle', 'spreadsheet', 'automation', 'stock', 'chatgpt']}, './youtube/google-ai-studio-free/readme.md': {'description': '(youtube정리) 무료 Google AI Studio, 유료 챗GPT에도 없는 기능 제공! 과연 답변 퀄리티는? / 구글 AI 제미나이(gemini) 2.0 사용법 총정리(실시간 화면 공유, 음성 대화, 검색 기능 등', 'tag': ['youtube', 'summary', 'my-summary', 'google', 'ai', 'gemini']}}
tag_count_dict =  defaultdict(<class 'int'>, {'git': 2, 'blame': 1, 'ai': 10, 'chatgpt': 3, 'notebooklm': 1, 'openai': 2, 'google': 2, '2025': 2, 'lge': 6, 'work': 7, 'history': 4, 'future': 3, 'my-life': 1, 'life': 2, 'direction': 1, 'log': 1, 'python': 11, 'meta-calss': 1, 'decorator': 1, 'bash': 2, 'education': 9, 'study': 1, '김진형': 1, '김인중': 1, 'machine-learning': 1, 'dreamhack': 1, 'girhub': 1, 'private': 1, 'scripts': 2, 'tax': 1, 'doxygen': 2, 'xml': 1, 'parsing': 1, 'clean-code': 2, 'comments': 1, 'docstring': 1, '': 5, '2022': 2, '2021': 1, 'Popen': 1, 'subprocess': 1, 'airflow': 1, 'etl': 1, 'recruit': 1, 'resume': 1, 'diary': 1, '2023': 3, 'memo': 3, 'run': 5, 'csv': 5, 'markdown': 4, 'convert': 5, 'mouse': 1, 'performance': 1, 'check': 2, 'aloga': 2, 'docker': 2, 'c++': 3, 'memory': 1, 'leak': 1, 'RAII': 1, 'vbee': 1, 'tcmd': 2, 'chart.js': 1, 'google-chart': 1, 'mixed': 1, 'TIDL': 1, 'md': 1, 'elice.io': 1, 'data': 2, 'analysis': 1, 'book': 9, '쿠버네티스': 1, 'kubernetes': 1, 'devops': 1, 'github': 2, 'clean': 1, 'code': 1, 'duplication': 1, 'TAF': 1, 'automation': 2, 'todo': 2, 'cisco': 1, 'cli': 1, '2024': 2, 'CDP': 1, 'english': 1, 'somedaytalk': 1, 'unittest': 1, 'vscode': 2, 'runOnSave': 1, 'extension': 1, 'shortkey': 1, 'c': 1, 'waitpid': 1, 'zombie': 1, 'ebook': 1, 'code-analysis': 1, 'DE': 5, 'engineer': 1, 'data-science': 5, 'recommendation': 1, 'autohotkey': 1, 'mini-keyboard': 1, 'robot': 1, 'stock': 2, 'writing': 1, 'list': 4, 'reading': 1, 'summary': 11, 'my-summary': 11, 'bigData': 2, 'pandas': 1, 'algorithm': 1, 'problem': 1, 'solving': 1, 'design': 1, 'pattern': 1, 'architecture': 1, 'copilot': 2, 'ms365': 1, 'prompt': 1, 'langchain': 1, 'LLM': 1, 'youtube': 4, 'visualization': 1, 'apps': 1, 'goodle': 1, 'spreadsheet': 1, 'gemini': 1})


이 값을 가지고 network graph를 그려주는 html file을 만들어 달라. 
file_to_tag_dict의 key는 filepath이다. 
network graph에서의 쌍은 file_to_tag_dict의 key와 'tag' 값들이 될 것이다. 예로 ./git_console_analysis.md -> git , ./git_console_analysis.md -> blame 이 될 것이다. 
node는 filepath와 tag들이 될 것이다. circle size는 tag_count_dict로 해야한다.
description은 filepath node를 가리킬때 description 정보로 보여주면 될 것으로 보인다

이를 이용한 html을 만들어달라.
그리고, 이를 처리하는 python code로 달라.
"""

import os
import time
import sys
import csv
import argparse
from collections import defaultdict
import re
import json
from pyvis.network import Network

# Define colors for nodes
def get_color(node_type):
    if node_type == 'file':
        return 'yellow'
    elif node_type == 'tag':
        return 'lightgreen'
    return 'orange'

def get_shape(node_type):
    if node_type == 'file':
        return 'ellipse'
    return 'circle'

if __name__ == "__main__":
     #parser = argparse.ArgumentParser(description="Convert CSV to Markdown")
     #parser.add_argument("input_file", nargs='?', default="index.csv", help="Input CSV file")
     #parser.add_argument("output_file", nargs='?', default="index.md", help="Output Markdown file")
     #args = parser.parse_args()

    # 딕셔너리를 JSON 파일로 저장
    with open('get-all-description-and-tag.json', 'r') as json_file:
        print('read: get-all-description-and-tag.json ->  gadat')
        gadat = json.load(json_file)

    # Data (use your provided data here)
    file_to_tag_dict =  gadat['file_to_tag_dict']
    # Convert tags into counts (if not already calculated)
    tag_count_dict = gadat['tag_count_dict']

    # Initialize Pyvis Network
    graph = Network(height='1000px', width='100%', directed=True, notebook=True)
    
    # Add nodes and edges to the graph
    for filepath, info in file_to_tag_dict.items():
        description = info['description']
        tags = info['tag']
    
        # Add filepath node
        graph.add_node(filepath, label=filepath, title=description, size=100,color=get_color('file'),shape=get_shape('file'))
         #graph.add_node(filepath, label=filepath, title=description, size=100,color=get_color('file'),shape=get_shape('file'))
    
        # Add tag nodes and edges
        for tag in tags:
            tag_size = tag_count_dict[tag] * 5  # Scale the size
            graph.add_node(tag, label=tag, size=tag_size,color=get_color('tag'))
             #graph.add_node(tag, label=tag, size=tag_size,color=get_color('tag'),shape=get_shape('tag'))
            graph.add_edge(tag, filepath)
    
    # Generate the HTML file
    output_file = 'get-all-description-and-tag-network_graph.html'
    graph.show(output_file)
    
    print(f"HTML file generated: {output_file}")
    
