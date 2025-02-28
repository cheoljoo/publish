- description : clean code의 주석부분으로 어떻게 주석을 잘 쓸 것인지? 주석을 문서화 시키는 부분
- tag : clean-code , comments , docstring , 
- date : 2025-01-01

TOC
- [1. 더-나은-코드-주석을-위한-팁](#1-더-나은-코드-주석을-위한-팁)
  - [1.1. AI 활용하기](#11-ai-활용하기)
  - [1.2. clean code](#12-clean-code)
- [2. comments로부터 문서를 자동생성](#2-comments로부터-문서를-자동생성)


---------------------

# 1. [더-나은-코드-주석을-위한-팁](https://wgkang80.tistory.com/entry/%EB%8D%94-%EB%82%98%EC%9D%80-%EC%BD%94%EB%93%9C-%EC%A3%BC%EC%84%9D%EC%9D%84-%EC%9C%84%ED%95%9C-13%EA%B0%80%EC%A7%80-%ED%8C%81)
- paragraph 별 주석을 이용하라.
- 요점만 언급하라.
- 일관된 양식을 사용하라.
- 내부적인 목적을 위한 태그를 사용하라. ex) todo
- 코드를 작성하는 동안 주석을 달아라. 따로 작성할 생각마라.
  - 가능하면 주석을 먼저 작성하고 코드를 작성하라.
- 코드를 갱신하면 주석을 갱신하라.
- 읽기 쉬운 코드가 주석보다 더 좋다.

## 1.1. AI 활용하기
- AI 주석 생성기를 사용하면 특정 표준에 따라 일관된 형식으로 주석을 만들 수 있음
- 전체 프로젝트에서 주석의 일관성을 유지할 수 있어 코드의 가독성 향상
- 활용하면 좋을 AI 주석 생성기: [Readable](https://readable.so/)

## 1.2. clean code
- [클린-코드-4-주석](https://rudaks.tistory.com/entry/%ED%81%B4%EB%A6%B0-%EC%BD%94%EB%93%9C-4-%EC%A3%BC%EC%84%9D)

# 2. comments로부터 문서를 자동생성
- python : docstring
  - [Docstring에 대하여](https://kimjingo.tistory.com/178)
  - [python docstrings](https://www.geeksforgeeks.org/python-docstrings/)
  - example : [cisco-style-cli.py](https://github.com/cheoljoo/fish/blob/6e11a5f477987ea1f6b2bf3186109bf42b2882c1/package/CiscoStyleCli/CiscoStyleCli.py)
- bash : bash도 docstring에 맞추어 주석을 써두면 어떻게든 활용 가능하게 만들수 있다.