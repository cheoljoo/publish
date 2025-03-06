# - description : copy first then remove unproper files when this file tag has --remove_tag
# - tag : python , classification

import os
import re
import time
import sys
import csv
import argparse
import json
import shutil

# 로그 파일 설정
workspace_folder = os.getenv('WORKSPACE_FOLDER', os.getcwd())
log_file = os.path.join(workspace_folder, "script_log.txt")

def log(message):
    try:
        print(f"{time.ctime()}: {message}", file=sys.stdout)
    except Exception as e:
        print(f"Failed to write to log file: {e}", file=sys.stderr)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="remove md fils with [--remove_tags]")
    parser.add_argument("--dir", nargs='?', default="../github_publish/memo", help="directory location to move file with [--remove_tags]")
    parser.add_argument("--remove_tags", nargs='?', default="private,lge", help="[--dir] does not have md files with [--remove_tags]") # default : github_publish can not have md files with tag : private or lge
    # --dir=../github_publish --remove_tags=private,lge
    # --dir=../mod_publish --remove_tags=private
    args = parser.parse_args()

    dir = args.dir
    remove_tags = args.remove_tags.split(',')

    print(f"dir: {dir}")
    print(f"remove_tags: {remove_tags}")

    descRe = re.compile('^\s*#?\s*-\s*description\s*:\s*(?P<s>.*$)')
    tagRe = re.compile('^\s*#?\s*-\s*tag\s*:\s*(?P<s>.*$)')
    dateRe = re.compile('^\s*#?\s*-\s*date\s*:\s*(?P<s>.*$)')

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
                

