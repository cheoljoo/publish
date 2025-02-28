#!/bin/bash
# - description : csv를 md로 변환시켜주는 convert bash로써 여기서는 실제로 각 directory에 맞는 convert_csv_to_md*.py 를 수행하는 script이다.
# - tag : csv , md , convert

# 현재 디렉토리 및 하위 디렉토리에서 검색
for dir in */; do
    # 디렉토리인지 확인
    if [ -d "$dir" ]; then
        # 해당 디렉토리 안에 convert_csv_to_md*.py 파일이 있는지 확인
        if ls "$dir"/convert_csv_to_md*.py 1> /dev/null 2>&1; then
            # 파일이 존재하면 디렉토리 이름 출력
            echo "  --> $dir"
            cd $dir
            python3 convert_csv_to_md*.py
            cd ..
        fi
    fi
done
