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
