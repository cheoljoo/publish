- description : git contribution 방법 / git repository 옮기기 / push commit 변경 등 git 관련 사항 들 정리
- tag : git , github
- date : 2023-01-01

# [git] github 협업을 위한 fork 부터 upstream 설정까지
- https://wonit.tistory.com/368

## setup
- $ git remote add upstream https://github.com/doxygen/doxygen
- $ git remote -v

## sync
- local download
    - $ git fetch upstream
- merge
    - $ git merge upstream/master
- push
    - $ git push origin master


# Git에서 가장 최근에 push한 커밋 메시지를 변경
- Git에서 가장 최근에 push한 커밋 메시지를 변경하려면 아래 단계를 따라야 합니다. 단, 이미 공개된 저장소에 push한 커밋의 메시지를 변경하는 것은 다른 사람들의 작업에 영향을 줄 수 있으므로 주의가 필요합니다.
- 최근 커밋 편집:
    - git commit --amend 명령어를 사용하여 가장 최근의 커밋 메시지를 편집합니다.
    - 이 명령은 기본 텍스트 편집기를 열어 현재 커밋 메시지를 보여줍니다.
    - 텍스트 편집기에서 메시지를 수정한 후 저장하고 닫습니다.
    - 변경된 커밋 강제 Push:
        - git push --force 또는 git push --force-with-lease 명령어를 사용하여 변경된 커밋을 원격 저장소에 강제로 push합니다.
        - --force-with-lease 옵션은 다른 사람이 이미 변경한 내용이 있는지 확인한 후 push하므로 더 안전합니다.
    - 명령어
        - git commit --amend -m "새로운 커밋 메시지"
        - git push --force-with-lease origin [브랜치명]



## https://wonit.tistory.com/368
- git remote add upstream https://github.com/doxygen/doxygen.git
- git remote -v
- git fetch upstream
- git merge upstream/master
- git push

## git repository 옮기기
- [GIT] Git Repository 옮기기 - https://yoshikixdrum.tistory.com/310#toc1