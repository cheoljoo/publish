# - description : book 관련 csv내용을 markdown으로 변환하는 프로그램
# - tag : book , python , run , csv , markdown , convert

import os
import time
import sys
import csv
import argparse

# 로그 파일 설정
workspace_folder = os.getenv('WORKSPACE_FOLDER', os.getcwd())
log_file = os.path.join(workspace_folder, "script_log.txt")

def log(message):
    try:
        print(f"{time.ctime()}: {message}", file=sys.stdout)
    except Exception as e:
        print(f"Failed to write to log file: {e}", file=sys.stderr)


# # 디버깅 출력
# print(f"Workspace folder: {workspace_folder}", file=sys.stderr)
# print(f"Log file path: {log_file}", file=sys.stderr)

# # 실행 로그 기록
# log("Script started.")
# log("Processing CSV file...")
# # (CSV 처리 코드 삽입)
# log("Script completed.")

# # 현재 작업 디렉토리 기록
# current_directory = os.getcwd()
# log(f"Current working directory: {current_directory}")
# print(f"Current working directory: {current_directory}", file=sys.stderr)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert CSV to Markdown")
    parser.add_argument("input_file", nargs='?', default="index.csv", help="Input CSV file")
    parser.add_argument("output_file", nargs='?', default="index.md", help="Output Markdown file")
    args = parser.parse_args()

#input_file = os.path.join(workspace_folder, "memo/book",args.input_file)
#output_file = os.path.join(workspace_folder,"memo/book", args.output_file)
    input_file = args.input_file
    output_file = args.output_file

    log(f"Input file: {input_file}")
    log(f"Output file: {output_file}")

    with open(input_file, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows_by_ongoing = {}
        
        # Group rows by Categories
        for row in reader:
            ongoing = row.get("Ongoing", "Unknown")
            if ongoing not in rows_by_ongoing:
                rows_by_ongoing[ongoing] = []
            rows_by_ongoing[ongoing].append(row)
        
        with open(output_file, "w", encoding="utf-8") as output:
            output.write('- description : book review : 읽은 책 내용 정리\n')
            output.write('- tag : book , list\n')
            output.write('\n<H1>Read Book Lists</H1>\n\n')
            output.write('- [index.csv](./index.csv)\n')
            
            # Write rows grouped by Categories and sorted by Date
            for ongoing, rows in rows_by_ongoing.items():
                output.write(f"\n# {ongoing}\n")
                sorted_rows = sorted(rows, key=lambda x: x["Date"])

                for row in sorted_rows:
                     #latin1_encoded = row['Title'].encode('latin-1')
                     #utf8_string = latin1_encoded.decode('utf-8', errors='replace')
                    utf8_string = row['Title']
                    # print('utf8',utf8_string)
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

    log("CSV to Markdown conversion completed.")
