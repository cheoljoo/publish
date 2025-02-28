- description : vscode 관련 나의 정리
- tag : vscode , shortkey
- date : 2022-01-01

TOC
- [1. vscode](#1-vscode)
  - [1.1. 2022-11-19 copilot](#11-2022-11-19-copilot)
  - [1.2. useful extensions](#12-useful-extensions)
  - [1.3. 2022-11-20 how to create extensions](#13-2022-11-20-how-to-create-extensions)
  - [1.4. Fast Developing : Don't Use the Sidebar in VS Code!!](#14-fast-developing--dont-use-the-sidebar-in-vs-code)
  - [1.5. 2022-11-20 how to create extensions](#15-2022-11-20-how-to-create-extensions)
  - [1.6. vscode shortkey](#16-vscode-shortkey)


------------------

# 1. vscode

## 1.1. 2022-11-19 copilot

## 1.2. useful extensions
- mako
  - https://github.com/marconi/mako-tmbundle
- clipboard
  

## 1.3. 2022-11-20 how to create extensions
- How to Create a VSCode Extension https://www.youtube.com/watch?v=4tk0Ak-dEjs&ab_channel=BenAwad
  - https://github.com/benawad/synonym-finder-vscode-extension
- LIVE 🔴: Build your first VS Code extension : https://www.youtube.com/watch?v=PGAu06_E_BU&ab_channel=VisualStudioCode
  - Join Tyler as he goes from just an idea to a published extension on the VS Code Marketplace. You’ll learn how to get started on building VS Code extensions, where to find resources, and how to publish them.
    - VS Code extension API documentation: https://code.visualstudio.com/api?WT.mc_id=devcloud-18509-cxa
    - Samples: https://github.com/microsoft/vscode-extension-samples
    - The extension we built: https://marketplace.visualstudio.com/items?itemName=TylerLeonhardt.vscode-types-installer-helper&WT.mc_id=devcloud-18509-cxa
    - Source code for the extension: https://github.com/TylerLeonhardt/vscode-types-installer-helper
  - getting started
    - https://code.visualstudio.com/api/get-started/your-first-extension -> npm install -g yo gnerator-code
    - yo code
      - TypeScript ...
- Creating a VS Code Extension basic snippets : https://www.youtube.com/watch?v=xgkDVUL0MxM&ab_channel=EvanDoesTech
  - great explanation!!
- How To Create And Deploy A VSCode Extension : https://www.youtube.com/watch?v=q5V4T3o3CXE&ab_channel=WebDevSimplified
  - publishing
- [VSCode Extension 만들기 - 1](https://wearee.tistory.com/88#:~:text=%EA%B0%84%EB%8B%A8%ED%9E%88%20%EC%84%A4%EB%AA%85%ED%95%98%EB%A9%B4%20package.json,%EC%9D%B5%EC%8A%A4%ED%85%90%EC%85%98%EC%9D%84%20%EC%8B%A4%ED%96%89%ED%95%B4%EB%B3%B4%EC%A3%A0.&text=%EC%9D%B4%EB%95%8C%20%EC%95%8C%EB%A6%BC%EC%B0%BD%EC%9D%B4%20%EB%9C%A8%EB%A9%B4%20Debug,VSCode%EA%B0%80%20%EB%9C%B0%20%EA%B2%83%EC%9E%85%EB%8B%88%EB%8B%A4.)
- [토이 프로젝트 - VSCode Extension 제작](https://tibetsandfox.tistory.com/38)
- [VS Code Extension 개발하기](https://medium.com/frontend-developers/vs-code-extension-%EA%B0%9C%EB%B0%9C%ED%95%98%EA%B8%B0-ae933343d2b5)
- [Your First Extension](https://code.visualstudio.com/api/get-started/your-first-extension)

## 1.4. Fast Developing : Don't Use the Sidebar in VS Code!!
- https://www.youtube.com/watch?v=s3H6PmB4SZ4&ab_channel=JamesQQuick
- If you want to write code faster, don't use the Sidebar in VS Code. It will slow you down! As a developer, your goal should be to keep your hands off of the mouse as much as possible. To do that, you should learn to use the built-in shortcuts in VS Code as well as a few amazing extensions. Learn how you can work with your files in VS Code without using the File Explorer or the Sidebar.
  - ^+w
  - ^+p  : open file
  - ^+tab : move tab
  - extension : advanced new file
    - ^+P  -> new file    or ^+n
  - extension : file utils : rename , move
- https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf
- shortcuts : https://www.youtube.com/watch?v=ifTF3ags0XI&ab_channel=Fireship
  - ^+shift+.  ^+> : list of functions
  - ^+P  -> @ or #  find symbol in javascript
  - extensions : auto rename tag for html
  - ^+l : highlight
  - extension : better comments
  - ^+P -> task : Configure default build task
  - extension : gitlens
  - remote repositories
  - extension : awesome flutter snippets
- [코딩시간을 절반으로 줄여주는 VSCode 9개 기능](https://www.youtube.com/watch?v=mh-0twurNRE&ab_channel=%EC%BD%94%EB%94%A9%EC%95%A0%ED%94%8C)
  - F12  or Alt+F12  : 바로 jump
    - css에서 사용하기 위해 설치 : CSS peak , HTML CSS Support
  - ^+R : refactoring : css에서는 함수 선언을 추가함
  - rename symbol : F2 (rename symbol in right click)
  - snippets : 자동완성
    - react extension : react  snippets
  - tabnine AI extension : 코드 추천  (월 1만원)
  - multi cursor : ALT+Click
  - emmet 명령어 + TAB
    - ex)   div>p*3
  - ^+방향키
  - ^+L : highlight 한줄
  - ^+p : file 이름
  - alt+down , alt+shift+down
  - extension : power mode
    - 뭐가 휘앙찬란...


## 1.5. 2022-11-20 how to create extensions
- How to Create a VSCode Extension https://www.youtube.com/watch?v=4tk0Ak-dEjs&ab_channel=BenAwad
  - https://github.com/benawad/synonym-finder-vscode-extension
- LIVE 🔴: Build your first VS Code extension : https://www.youtube.com/watch?v=PGAu06_E_BU&ab_channel=VisualStudioCode
  - Join Tyler as he goes from just an idea to a published extension on the VS Code Marketplace. You’ll learn how to get started on building VS Code extensions, where to find resources, and how to publish them.
    - VS Code extension API documentation: https://code.visualstudio.com/api?WT.mc_id=devcloud-18509-cxa
    - Samples: https://github.com/microsoft/vscode-extension-samples
    - The extension we built: https://marketplace.visualstudio.com/items?itemName=TylerLeonhardt.vscode-types-installer-helper&WT.mc_id=devcloud-18509-cxa
    - Source code for the extension: https://github.com/TylerLeonhardt/vscode-types-installer-helper
  - getting started
    - https://code.visualstudio.com/api/get-started/your-first-extension -> npm install -g yo gnerator-code
    - yo code
      - TypeScript ...
- Creating a VS Code Extension basic snippets : https://www.youtube.com/watch?v=xgkDVUL0MxM&ab_channel=EvanDoesTech
  - great explanation!!
- How To Create And Deploy A VSCode Extension : https://www.youtube.com/watch?v=q5V4T3o3CXE&ab_channel=WebDevSimplified
  - publishing

## 1.6. vscode shortkey
- 파일 or 창 선택 : ^+1 , , ^+2
- 여러줄의 앞에 -을 삽입 : 
  - Multi-Line Editing with same string : Ctrl + Alt + Arrow Keys
- Multi-Line Editing : Alt + Multiple mouse point
- 블럭을 잡이서 한번에 editing : alt+shift+마우스 drag
- 일정 pattern을 다 잡고 싶을때 , 해당 글자를 잡아서 ^+D 를 여러번 잡고 싶은 만큼
