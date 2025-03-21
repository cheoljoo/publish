# - description : create revision.md
# - tag : python , classification

import os
import re
import time
import sys
import csv
import argparse
import json
import shutil
import subprocess
from datetime import datetime



if __name__ == "__main__":
    revisionDict = {}
    with open('revision.json', 'r') as json_file:
        print('read: revision.json ->  revisionDict')
        revisionDict = json.load(json_file)


    # Git 명령어 실행
    result = subprocess.run(
        ["git", "status"],    # "--untracked-files=no"],
        capture_output=True,  # 출력을 변수에 저장
        text=True,            # 문자열로 변환
        check=True            # 오류 발생 시 예외 발생
    )

    # 결과를 변수에 저장
    git_status_output = result.stdout

    now = str(datetime.now())  # 현재 날짜 및 시간 가져오기
    newfileRe = re.compile('^\s*new file:\s*"?(?P<s>.*$)')
    modifiedRe = re.compile('^\s*modified:\s*"?(?P<s>.*$)')
    descRe = re.compile('^\s*#?\s*-\s*description\s*:\s*(?P<s>.*$)')
    tagRe = re.compile('^\s*#?\s*-\s*tag\s*:\s*(?P<s>.*$)')
    dateRe = re.compile('^\s*#?\s*-\s*date\s*:\s*(?P<s>.*$)')
    newFileStartRe = re.compile('\s*(use "git add <file>..." to include in what will be committed)')
    newFileStartFlag = False
    for line in git_status_output.split('\n'):
        print(newFileStartFlag,line)
        if newFileStartRe.search(line):
            newFileStartFlag = True
            continue
        if newFileStartFlag == False:
            t = newfileRe.search(line)
            if t:
                filename = t.group(1)
                filename = filename.encode('latin1').decode('unicode_escape')
                filename = filename.encode('latin1').decode('utf-8')
                if filename.endswith('"'):
                    filename = filename[:-1]
                 #filename = re.sub(r'\\\\', r'\\', filename)
                print('added filename',filename)
                if filename not in ['revision.json','revision.md','TOC.md','README.md'] and (filename.endswith('.md') or filename.endswith('.py')):
                    if now not in revisionDict:
                        revisionDict[now] = []
                    revisionDict[now].append( {'type':'new file:','value':filename } )
            t = modifiedRe.search(line)
            if t:
                filename = t.group(1)
                filename = filename.encode('latin1').decode('unicode_escape')
                filename = filename.encode('latin1').decode('utf-8')
                 #print('filename',filename)
                if filename.endswith('"'):
                    filename = filename[:-1]
                 #print('filename',filename)
                 #filename = re.sub(r'\\\\', r'\\', filename)
                print('modified filename',filename)
                if filename not in ['revision.json','revision.md','TOC.md','README.md'] and (filename.endswith('.md') or filename.endswith('.py')):
                    if now not in revisionDict:
                        revisionDict[now] = []
                    revisionDict[now].append( {'type':'modified:','value':filename } )
        else:
            filename = line.strip()
            filename = filename.encode('latin1').decode('unicode_escape')
            filename = filename.encode('latin1').decode('utf-8')
            if filename.endswith('"'):
                filename = filename[:-1]
            if filename.startswith('"'):
                filename = filename[1:]
            print('new_file filename',filename)
            if filename not in ['revision.json','revision.md','TOC.md','README.md'] and (filename.endswith('.md') or filename.endswith('.py')):
                if now not in revisionDict:
                    revisionDict[now] = []
                revisionDict[now].append( {'type':'new_file:','value':filename } )
    print('revisionDict:',revisionDict)
     #sortedRevisionList = sorted(revisionDict, key=lambda x: (x['date'], x['type']), reverse=True)
    sortedRevisionDict = dict(sorted(revisionDict.items(),reverse=True))

    print('sort:',sortedRevisionDict)
    for date,vv in sortedRevisionDict.items():
        for v in sortedRevisionDict.get(now,[]):
            print('sort v',v)
            descValue = ''
            filename = v['value']
            if filename.endswith('.md') or filename.endswith('.py'):
                descFlag = False
                tagFlag = False
                dateFlag = False
                 #print(os.getcwd())
                print('open filename',filename)
                with open(filename,'r',encoding="utf-8" ) as fr:
                    lines = fr.readlines()
                    MaxLineNumber = 10
                    lineNumber = 0
                    for line in lines:
                        t = descRe.search(line)
                        if t:
                            descFlag = True
                            descValue = t.group(1)
                             #print('selected',date,descValue,v)
                        t = tagRe.search(line)
                        if t:
                            tagFlag = True
                            tagValue = t.group(1)
                        t = dateRe.search(line)
                        if t:
                            dateFlag = True
                            dateValue = t.group(1)
                        lineNumber += 1
                        if lineNumber >= MaxLineNumber:
                            break
            v['desc'] = descValue

    with open('revision.json', "w", encoding="utf-8") as json_file:
        print('write: revision.json <- revisionDict')
        json.dump(sortedRevisionDict, json_file)

    with open('revision.md', "w", encoding="utf-8") as f:
        f.write('''- description : revision information : what is changed per date
- tag : revision , changes
- date : [today]

''')
        for date,vv in sortedRevisionDict.items():
            print('revision.md',date,vv)
            f.write('# {date}\n'.format(date=date))
            for v in vv:
                filename = v['value']
                if v.get('desc',''):
                    f.write('- {type} [{file}]({file}) : desc - {desc}\n'.format(type=v['type'] , file=filename, desc=v['desc']))
                else:
                    f.write('- {t} [{file}]({file})\n'.format(t=v['type'] , file=filename))
            f.write('\n')


