# - description : get all description and tag from memo sub-directories (output:get-all-description-and-tag.json)
# - tag : python , run , json , data

import os
import time
import sys
import csv
import argparse
from collections import defaultdict
import re
import json
import unicodedata
from googletrans import Translator


import string
from zlib import compress
import base64
maketrans = bytes.maketrans
plantuml_alphabet = string.digits + string.ascii_uppercase + string.ascii_lowercase + '-_'
base64_alphabet   = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
b64_to_plantuml = maketrans(base64_alphabet.encode('utf-8'), plantuml_alphabet.encode('utf-8'))
# plantuml encoding
def deflate_and_encode(plantuml_text):
    """
    plantuml encoding
    zlib compress the plantuml text and encode it for the plantuml server.
    """
    zlibbed_str = compress(plantuml_text.encode('utf-8'))
    compressed_string = zlibbed_str[2:-4]
    return base64.b64encode(compressed_string).translate(b64_to_plantuml).decode('utf-8')


def remove_non_utf8_regex(text):
    return re.sub(r'[^\x00-\x7F\u0080-\uFFFF]', '', text)

def remove_non_utf8_unicodedata(text):
    return ''.join(c for c in text if unicodedata.category(c) not in ['Co', 'Cs'])

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def remove_non_ascii(s):
    return ''.join(c for c in s if ord(c) < 128)

if __name__ == "__main__":
     #parser = argparse.ArgumentParser(description="Convert CSV to Markdown")
     #parser.add_argument("input_file", nargs='?', default="index.csv", help="Input CSV file")
     #parser.add_argument("output_file", nargs='?', default="index.md", help="Output Markdown file")
     #args = parser.parse_args()

    translator = Translator()

    descRe = re.compile('^\s*#?\s*-\s*description\s*:\s*(?P<s>.*$)')
    tagRe = re.compile('^\s*#?\s*-\s*tag\s*:\s*(?P<s>.*$)')
    dateRe = re.compile('^\s*#?\s*-\s*date\s*:\s*(?P<s>.*$)')
    file_to_tag_dict = {}
    tag_count_dict = defaultdict(int)

    tag_json = {}
    
    # 현재 디렉토리와 하위 디렉토리의 모든 파일 경로 출력
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.md') or file.endswith('.py') or file.endswith('.sh'):
                 #print(os.path.join(root, file))
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
                         #print(filepath)
                         #print('  ',descValue.strip())
                        tags = [ i.strip() for i in tagValue.split(',') ]
                         #print('  ',tags)
                        for tag in tags:
                            tag_count_dict[tag] += 1
                         #print(lines[:5])
                        if filepath not in file_to_tag_dict:
                            file_to_tag_dict[filepath] = {}
                        file_to_tag_dict[filepath]['description'] = descValue.strip()
                        file_to_tag_dict[filepath]['tag'] = tags
            elif file.strip() == 'tag.json':
                filepath = os.path.join(root, file)
                with open(filepath,'r',encoding="utf-8") as json_file:
                    print('read: {f} ->  gadat'.format(f=filepath))
                    csv_tag = json.load(json_file)
                    tag_json[root] = csv_tag
    print('=============== first 5 items ==============')
    print('file_to_tag_dict = ',list(file_to_tag_dict.items())[:5], ' ...')
    print('tag_count_dict = ',list(tag_count_dict.items())[:5], ' ...')
    get_all_description_and_tag = {'file_to_tag_dict':file_to_tag_dict , 'tag_count_dict':tag_count_dict}

    # 딕셔너리를 JSON 파일로 저장
    with open('get-all-description-and-tag.json', 'w') as json_file:
        print('write : get-all-description-and-tag.json <- get-all-description-and-tag')
        json.dump(get_all_description_and_tag, json_file)
    
    trans_dict = {}
    if os.path.exists('get-all-description-and-tag-trans.json'):
        with open('get-all-description-and-tag-trans.json','r',encoding="utf-8") as json_file:
            print('read: {f} -> trans_dict'.format(f='get-all-description-and-tag-trans.json'))
            trans_dict = json.load(json_file)

    with open('TOC.md','w') as f:
        print('write : TOC.md <- TOC in memo')
        f.write('# memo TOC\n')
        for fttdk , fttdv in sorted(file_to_tag_dict.items()):
            f.write('- [{a}]({b}) : {c}\n'.format(b=fttdk,a=fttdk.lstrip("./"),c=fttdv['description']))

        for tag_dir , tag_v in sorted(list(tag_json.items())):
            tag_dir = tag_dir.encode('utf-8', errors='ignore').decode('utf-8')
            f.write('\n# [{d}]({d}/index.md)\n'.format(d=tag_dir))
            for tag_category , tag_items in sorted(list(tag_v.items())):
                tag_category = tag_category.encode('utf-8', errors='ignore').decode('utf-8')
                f.write('\n## category : {d}\n'.format(d=tag_category))
                items = sorted(tag_items, key=lambda x: x["Date"])
                for row in items:
                    row_title = row['Title'].encode('utf-8', errors='ignore').decode('utf-8')
                    if not is_ascii(row_title):
                        if row_title not in trans_dict:
                            res = translator.translate(row_title, src='ko', dest='en')
                            print(row_title , '->',res.text)
                            trans_dict[row_title] = remove_non_ascii(res.text)
                            row_title = remove_non_ascii(res.text)
                        else:
                            row_title = trans_dict[row_title]
                    f.write(f"### {row_title} ({row['Date']})\n")
                    for column_name, column_value in row.items():
                        if column_value:
                            if column_name == "Title":
                                f.write(f"- {column_name}: [{column_value}]({row['URL']})\n")
                            elif column_name == "URL":
                                pass
                            elif column_name == "NotesLink":
                                f.write(f"- [{column_name}]({column_value})\n")
                            else:
                                f.write(f"- {column_name}: {column_value}\n")
                    f.write("\n")
        f.write("\n")
        plantuml_text = ''
        with open('total.md', 'r') as totalFd:
            lines = totalFd.readlines()
            plantuml_text = '\n'.join(lines[1:-1])
        f.write("""
# process Map
- svg through tiger02.lge.com server
  - ![](http://tiger02.lge.com:18080/svg/{plantuml})
- png through www.plantuml.com
  - ![](https://www.plantuml.com/plantuml/png/{plantuml})

""".format(plantuml=deflate_and_encode(plantuml_text)))
        # read total.md
        # make a link using def deflate_and_encode(plantuml_text):

    with open('get-all-description-and-tag-trans.json', 'w') as json_file:
        print('write : get-all-description-and-tag-trans.json <- trans_dict')
        json.dump(trans_dict, json_file)

