- description : my private jira site in atlassian - how to use restapi / outlook mail to atlassian jira
- tag : jira , atlassian , restapi , token
- date : 2025-01-01

TOC
- [1. account](#1-account)
  - [1.1. information](#11-information)
- [2. rest api](#2-rest-api)
- [3. outlook 과 Atlassian JIRA 연결](#3-outlook-과-atlassian-jira-연결)
  - [3.1. jira 계정 (server)](#31-jira-계정-server)
  - [3.2. outlook](#32-outlook)


-------------------


# 1. account
- it is free for all.  However it starts with premium level within 1 month.
- we can use all function in 1 month.

## 1.1. information
- id : 쥐메일
- URL : https://cheoljoo.atlassian.net
- api token : ```secreat_key.md 1.```
  - expire date : 2016.2.10   we need to update api token every year.
- kanban name : KAN

# 2. rest api
- source
```python
# -*- coding:utf-8 -*-
# reference
# https://community.atlassian.com/t5/Jira-questions/Using-Rest-API-how-do-I-get-all-issues-open-closed-from-a-Kanban/qaq-p/721908

import optparse
import requests
from requests.auth import HTTPBasicAuth
import json
import sys

auth = HTTPBasicAuth("cheoljoo@gmail.com", "secreat_key.md 1.")
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "charset":"utf8"
}

def test():
    response = requests.get("https://cheoljoo.atlassian.net/rest/api/2/search?jql=project=KAN&maxResults=100&startAt=0",
                            headers=headers,
                            auth=auth)

    test = json.loads(response.text)
    for t in test["issues"]:
        issue_name = t["fields"]["summary"]
        print("issue_name : {}, issue_id : {}, issue_key : {}".format(issue_name, t["id"], t["key"]))

def main():
    test()

main()
```

- result
```txt
$  python3 cc.py
issue_name : [헬로비젼 KB 카드](./todo-2025.md#4-집에서-해야-할-일), issue_id : 10012, issue_key : KAN-8
issue_name : 재실 센서 [구매](./todo-2025.md#6-구매), issue_id : 10011, issue_key : KAN-7
issue_name : GV80 구정 이후 세차 6회 사용 예약 : [상세](./gv80-my-car.md), issue_id : 10010, issue_key : KAN-6
issue_name : 안 쓰는 볼펜 정리, issue_id : 10009, issue_key : KAN-5
issue_name : replit을 이용한 주식 분석 프로그램 만드는 과정 작성하기 및 backtest 수정, issue_id : 10008, issue_key : KAN-4
issue_name : problem solving 문제 정리 : youtube 가능한 것 먼저 만들기 .. 앞에서부터 순서로대로 푼 문제를 다룰 필요없다. 최근에 푼 것 먼저 처리하자., issue_id : 10007, issue_key : KAN-3
issue_name : github.io를 다시 살리자. blog를 위한. markdown을 꼭 지원해야 한다. github.io에서도 처리되는 요약 필요 (make.com 자동화까지 고려 필요), issue_id : 10006, issue_key : KAN-2
issue_name : 자산폐기 3단계 GERP에서 자산 list 지우기, issue_id : 10005, issue_key : KAN-1
```

# 3. outlook 과 Atlassian JIRA 연결
- outlook plugin 에서 jira cloud를 설정하면 https://cheoljoo.atlassian.net (web)에서 보듯이 outlook에서 jira page를 볼수 있다.

## 3.1. jira 계정 (server)
- https://cheoljoo.atlassian.net/jira/marketplace/discover/app/de.catworkx.jira.plugins.outlook2jira?installDialogOpen=true&source=mpac
- 를 add 해서 outlook과 연동 할수 있는 package를 add한다.

## 3.2. outlook
- ![outlookplugin](../img/image-4.png)  Outlook Plugin 에서 Jira Could For Outlook (Official) 이나 Jira for Outlook 을 설치하여 사용한다.
  - id는 atlassian의 email을 입력하고 , API token은 받으면 된다.
  - 그림에서와 같이 Jira Could For Outlook (Official) 이나 Jira for Outlook 을 선택하여 ticket을 생성하면 jira atlassian에서 생성된 ticket을 볼 수 있다.

> 잘 생성된다. 

