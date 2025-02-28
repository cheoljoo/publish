# - description : book 관련 csv내용을 markdown으로 변환하는 프로그램
# - tag : book , python , run , csv , markdown , convert

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


'''
get-all-description-and-tag-to-network-graph.py:    with open('get-all-description-and-tag.json', 'r') as json_file:
get-all-description-and-tag-to-network-graph.py:        print('read: get-all-description-and-tag.json ->  gadat')
get-all-description-and-tag-to-network-graph.py:        gadat = json.load(json_file)
remove_files.py:import json
remove_files.py:            with open(tfile, "w", encoding="utf-8") as json_file:
remove_files.py:                json.dump(rows_by_category, json_file)
'''



if __name__ == "__main__":
    revisionDict = {}
    with open('revision.json', 'r') as json_file:
        print('read: revision.json ->  revisionDict')
        revisionDict = json.load(json_file)


    # Git 명령어 실행
    result = subprocess.run(
        ["git", "status", "--untracked-files=no"],
        capture_output=True,  # 출력을 변수에 저장
        text=True,            # 문자열로 변환
        check=True            # 오류 발생 시 예외 발생
    )

    # 결과를 변수에 저장
    git_status_output = result.stdout

    now = str(datetime.now())  # 현재 날짜 및 시간 가져오기
    newfileRe = re.compile('^\s*new file:\s*(?P<s>.*$)')
    modifiedRe = re.compile('^\s*modified:\s*(?P<s>.*$)')
    descRe = re.compile('^\s*#?\s*-\s*description\s*:\s*(?P<s>.*$)')
    tagRe = re.compile('^\s*#?\s*-\s*tag\s*:\s*(?P<s>.*$)')
    dateRe = re.compile('^\s*#?\s*-\s*date\s*:\s*(?P<s>.*$)')
    for line in git_status_output.split('\n'):
        t = newfileRe.search(line)
        if t:
            if now not in revisionDict:
                revisionDict[now] = []
            revisionDict[now].append( {'type':'new file:','value':t.group(1).strip() } )
        t = modifiedRe.search(line)
        if t:
            if now not in revisionDict:
                revisionDict[now] = []
            revisionDict[now].append( {'type':'modified:','value':t.group(1).strip() } )
    print('revisionDict:',revisionDict)
     #sortedRevisionList = sorted(revisionDict, key=lambda x: (x['date'], x['type']), reverse=True)
    sortedRevisionDict = dict(sorted(revisionDict.items(),reverse=True))
    with open('revision.json', "w", encoding="utf-8") as json_file:
        print('write: revision.json <- revisionDict')
        json.dump(sortedRevisionDict, json_file)

    with open('revision.md', "w", encoding="utf-8") as f:
        f.write('''- description : revision information : what is changed per date
- tag : revision , changes
- date : [today]

''')
        for date,vv in sortedRevisionDict.items():
            f.write('# {date}\n'.format(date=date))
            print(vv)
            for v in vv:
                print('v',v)
                if v['value'].endswith('.md'):
                    descValue = 'none'
                    descFlag = False
                    tagFlag = False
                    dateFlag = False
                    with open(v['value'],'r',encoding="utf-8") as fr:
                        lines = fr.readlines()
                        MaxLineNumber = 10
                        lineNumber = 0
                        for line in lines:
                            t = descRe.search(line)
                            if t:
                                descFlag = True
                                descValue = t.group(1)
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
                    if descFlag and descValue:
                        f.write('- {type} {file} : desc - {desc}\n'.format(type=v['type'] , file=v['value'], desc=descValue))
                    else:
                        f.write('- {t} {v} : desc - none\n'.format(t=v['type'] , v=v['value']))
                else:
                    f.write('- {t} {v}\n'.format(t=v['type'] , v=v['value']))
            f.write('\n')



    quit(0)
    


    dir = args.dir
    remove_tags = args.remove_tags.split(',')

    print(f"dir: {dir}")
    print(f"remove_tags: {remove_tags}")



    remove_dir = []
    for root, dirs, files in os.walk(dir):
        print('r',root,'d',dirs,'f',files)
        countMovableFiles = 0
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                with open(filepath,'r',encoding="utf-8") as f:
                    lines = f.readlines()
                    descFlag = False
                    tagFlag = False
                    dateFlag = False
                    MaxLineNumber = 10
                    lineNumber = 0
                    for line in lines:
                        t = descRe.search(line)
                        if t:
                            descFlag = True
                            descValue = t.group(1)
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
                if descFlag and tagFlag:
                    existRemoveTag = False
                    tags = [ i.strip() for i in tagValue.split(',') ]
                    for remove_tag in remove_tags:
                        if remove_tag in tags:
                            existRemoveTag = True
                    if existRemoveTag == True:
                        print('remove file:',filepath)
                        os.remove(filepath)
                    else:
                        countMovableFiles += 1
        print(root,files,'[cmf]',countMovableFiles)
        if len(dirs) == 0 and countMovableFiles == 0:
            print('remove directory:',root)
            shutil.rmtree(root)
                

    quit()
    

    directories = [d for d in os.listdir('.') if os.path.isdir(d) and os.path.exists(d+'/'+input_file)]
    print('directories:',directories)
    for dir in directories:
        hfile = dir+'/'+header_file
        ifile = dir+'/'+input_file
        ofile = dir+'/'+output_file
        tfile = dir+'/'+tag_file
        header = []
        if os.path.exists(hfile):
            with open(hfile, "r", encoding="utf-8") as file:
                header = file.readlines()
        header = ''.join(header)
        print('dir:',dir)
        print('header:',header)
        with open(ifile, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows_by_category = {}
        
            # Group rows by Categories
            for row in reader:
                category = row.get("Categories", "Uncategorized")
                if category not in rows_by_category:
                    rows_by_category[category] = []
                rows_by_category[category].append(row)
            
            with open(ofile, "w", encoding="utf-8") as output:
                output.write(header)
                output.write('\n<H1>{d} Lists</H1>\n\n'.format(d=dir.upper()))
                output.write('- [index.csv](./index.csv)\n')
                
                # Write rows grouped by Categories and sorted by Date
                for category, rows in rows_by_category.items():
                    output.write(f"\n# {category}\n")
                    sorted_rows = sorted(rows, key=lambda x: x["Date"])
    
                    for row in sorted_rows:
                        output.write(f"## {row['Title']} ({row['Date']})\n")
                        for column_name, column_value in row.items():
                            if column_value:
                                if column_name == "Title":
                                    output.write(f"- {column_name}: [{column_value}]({row['URL']})\n")
                                elif column_name == "URL":
                                    pass
                                elif column_name == "NotesLink":
                                    output.write(f"- [{column_name}]({column_value})\n")
                                else:
                                    output.write(f"- {column_name}: {column_value}\n")
                        output.write("\n")

            with open(tfile, "w", encoding="utf-8") as json_file:
                json.dump(rows_by_category, json_file)
    
    log("CSV to Markdown conversion completed.")
