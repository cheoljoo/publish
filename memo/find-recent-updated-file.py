# - description : Git에서 추적하는 파일들 중에서 최근 수정된 파일들을 찾아 절대 경로와 함께 표시하는 스크립트입니다. 기본적으로 최근 30개 파일을 표시하며, 수정 날짜 순으로 정렬됩니다.
# - tag : python , file-list, git

"""
find-recent-updated-file.py

Git에서 추적하는 파일들 중에서 최근 수정된 파일들을 찾아 절대 경로와 함께 표시하는 스크립트입니다.
기본적으로 최근 30개 파일을 표시하며, 수정 날짜 순으로 정렬됩니다.
"""

import os
import sys
import subprocess
import argparse
from datetime import datetime
from pathlib import Path


def run_git_command(command, repo_path=None):
    """Git 명령어를 실행하고 결과를 반환합니다."""
    try:
        if repo_path:
            os.chdir(repo_path)
        
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        
        if result.returncode != 0:
            print(f"Git 명령어 실행 실패: {command}")
            print(f"오류 메시지: {result.stderr}")
            return None
        
        return result.stdout.strip()
    except Exception as e:
        print(f"명령어 실행 중 오류 발생: {e}")
        return None


def get_git_root():
    """현재 디렉토리에서 Git 저장소의 루트 경로를 찾습니다."""
    try:
        result = subprocess.run(
            ['git', 'rev-parse', '--show-toplevel'],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return None
    except Exception:
        return None


def get_git_tracked_files():
    """현재 디렉토리에서 Git에서 추적하는 파일 목록을 가져옵니다."""
    # 현재 디렉토리(.)에서 -z 옵션으로 NULL로 구분된 파일명을 가져와서 한글 파일명 문제 해결
    command = "git ls-files -z ."
    output = run_git_command(command)
    
    if output is None:
        return []
    
    # NULL 문자로 구분된 파일명들을 분리
    files = output.split('\0')
    return [f for f in files if f.strip()]


def get_file_modification_info(files, repo_root, verbose=False):
    """파일들의 수정 정보를 가져옵니다."""
    file_info = []
    processed_count = 0
    skipped_count = 0
    error_count = 0
    
    for file_path in files:
        # 현재 디렉토리에서 작업하므로 상대경로 사용
        if not os.path.exists(file_path):
            skipped_count += 1
            if verbose:
                print(f"파일이 존재하지 않음: {file_path}")
            continue
        
        try:
            # 파일 시스템의 수정 시간 가져오기
            mtime = os.path.getmtime(file_path)
            modification_date = datetime.fromtimestamp(mtime)
            
            # Git에서 마지막 커밋 정보 가져오기 (옵션)
            git_command = f'git log -1 --format="%ai" -- "{file_path}"'
            git_date_output = run_git_command(git_command)
            
            git_date = None
            if git_date_output:
                try:
                    # Git 날짜 포맷 파싱 개선: +0900 -> +09:00 형태로 변환
                    date_str = git_date_output.replace('"', '').strip()
                    
                    # "2025-08-08 09:03:11 +0900" 형태 처리
                    if ' ' in date_str and ('+' in date_str or '-' in date_str):
                        # 마지막 공백으로 날짜/시간 부분과 타임존 부분 분리
                        parts = date_str.rsplit(' ', 1)
                        if len(parts) == 2:
                            datetime_part = parts[0]  # "2025-08-08 09:03:11"
                            tz_part = parts[1]        # "+0900" 또는 "-0500"
                            
                            # 타임존 형태 변환: "+0900" -> "+09:00"
                            if len(tz_part) == 5 and (tz_part.startswith('+') or tz_part.startswith('-')):
                                sign = tz_part[0]
                                hours = tz_part[1:3]
                                minutes = tz_part[3:5]
                                tz_part = f"{sign}{hours}:{minutes}"
                            
                            # ISO 8601 형태로 변환: "2025-08-08T09:03:11+09:00"
                            iso_date = f"{datetime_part.replace(' ', 'T')}{tz_part}"
                            git_date = datetime.fromisoformat(iso_date)
                    # 이미 ISO 형태인 경우
                    else:
                        git_date = datetime.fromisoformat(date_str)
                        
                except Exception as e:
                    if verbose:
                        print(f"Git 날짜 파싱 실패: {file_path} - {e}")
                        print(f"  원본 날짜 문자열: '{git_date_output}'")
            
            file_info.append({
                'relative_path': file_path,
                'absolute_path': os.path.abspath(file_path),
                'file_mtime': modification_date,
                'git_date': git_date,
                'size': os.path.getsize(file_path)
            })
            processed_count += 1
            
        except Exception as e:
            error_count += 1
            if verbose:
                print(f"파일 정보 가져오기 실패: {file_path} - {e}")
            continue
    
    if verbose:
        print(f"파일 처리 통계: 처리됨={processed_count}, 건너뜀={skipped_count}, 오류={error_count}")
    
    return file_info


def get_file_description(file_path):
    """텍스트 파일의 첫 번째 줄에서 description을 추출합니다."""
    try:
        # 텍스트 파일인지 확인 (확장자 기준)
        text_extensions = {'.md', '.txt', '.py', '.js', '.html', '.css', '.json', '.xml', '.yaml', '.yml', '.csv'}
        _, ext = os.path.splitext(file_path.lower())
        if ext not in text_extensions:
            return None
            
        with open(file_path, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()
            
        # "- description :" 또는 "# - description :" 패턴 매칭
        # #? 는 #이 있을 수도 있고 없을 수도 있음을 의미
        import re
        pattern = r'^\s*#?\s*-\s*description\s*:\s*(.+)$'
        match = re.match(pattern, first_line, re.IGNORECASE)
        if match:
            return match.group(1).strip()
            
        return None
    except Exception:
        return None


def format_file_size(size_bytes):
    """파일 크기를 읽기 쉬운 형태로 포맷팅합니다."""
    if size_bytes < 1024:
        return f"{size_bytes}B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes/1024:.1f}KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes/(1024*1024):.1f}MB"
    else:
        return f"{size_bytes/(1024*1024*1024):.1f}GB"


def main():
    parser = argparse.ArgumentParser(
        description="Git에서 추적하는 파일들 중 최근 수정된 파일들을 찾습니다."
    )
    parser.add_argument(
        '-n', '--number',
        type=int,
        default=30,
        help='표시할 파일 개수 (기본값: 30)'
    )
    parser.add_argument(
        '-r', '--repo-path',
        type=str,
        help='Git 저장소 경로 (기본값: 현재 디렉토리)'
    )
    parser.add_argument(
        '--use-git-date',
        action='store_true',
        help='파일 시스템 날짜 대신 Git 커밋 날짜 사용'
    )
    parser.add_argument(
        '--show-size',
        action='store_true',
        help='파일 크기 정보 표시'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='상세한 디버그 정보 표시'
    )
    parser.add_argument(
        '--oneline',
        action='store_true',
        help='한 줄로 간단하게 표시 (번호. 시간 파일명)'
    )
    
    args = parser.parse_args()
    
    # Git 저장소 루트 찾기
    if args.repo_path:
        repo_root = os.path.abspath(args.repo_path)
        os.chdir(repo_root)
    else:
        repo_root = get_git_root()
    if not repo_root:
        print("현재 디렉토리가 Git 저장소가 아닙니다.")
        print("Git 저장소 내에서 실행하거나 --repo-path 옵션을 사용하세요.")
        sys.exit(1)

    if not args.oneline:
        print(f"Git 저장소: {repo_root}")
        print(f"최근 수정된 {args.number}개 파일을 찾는 중...\n")

    # Git에서 추적하는 파일 목록 가져오기
    tracked_files = get_git_tracked_files()
    if not tracked_files:
        print("Git에서 추적하는 파일을 찾을 수 없습니다.")
        sys.exit(1)

    if not args.oneline:
        print(f"총 {len(tracked_files)}개의 추적 파일 발견")    # 파일 수정 정보 가져오기
    file_info = get_file_modification_info(tracked_files, repo_root, args.verbose)
    
    if not file_info:
        print("파일 정보를 가져올 수 없습니다.")
        sys.exit(1)
    
    # 날짜 기준으로 정렬 (최신순)
    if args.use_git_date:
        # Git 날짜가 있는 파일들만 필터링하고 Git 날짜로 정렬
        file_info = [f for f in file_info if f['git_date'] is not None]
        file_info.sort(key=lambda x: x['git_date'], reverse=True)
        date_key = 'git_date'
        date_label = 'Git 커밋 날짜'
    else:
        # 파일 시스템 수정 날짜로 정렬
        file_info.sort(key=lambda x: x['file_mtime'], reverse=True)
        date_key = 'file_mtime'
        date_label = '파일 수정 날짜'
    
    # 상위 N개 파일 표시
    recent_files = file_info[:args.number]
    
    if not args.oneline:
        print(f"\n=== 최근 수정된 {len(recent_files)}개 파일 ({date_label} 기준) ===\n")
    
    for i, file_info in enumerate(recent_files, 1):
        date_str = file_info[date_key].strftime('%Y-%m-%d %H:%M:%S')
        size_str = f" ({format_file_size(file_info['size'])})" if args.show_size else ""
        
        if args.oneline:
            # 한 줄 형식: "1. 2025-08-08 09:03:11 (  9.7KB) relative/path/filename.py"
            # 크기를 고정 너비(8자리)로 정렬하여 파일명이 일정하게 정렬되도록 함
            if args.show_size:
                size_formatted = f"({format_file_size(file_info['size']):>7})"
                print(f"{i}. {date_str} {size_formatted} {file_info['relative_path']}")
            else:
                print(f"{i}. {date_str} {file_info['relative_path']}")
        else:
            # 기존 형식
            print(f"{i:2d}. {date_str}{size_str}")
            print(f"    {file_info['absolute_path']}")
            
            # 파일 description 표시 (텍스트 파일인 경우)
            description = get_file_description(file_info['relative_path'])
            if description:
                print(f"    Description: {description}")
            
            # Git 날짜와 파일 시스템 날짜가 다른 경우 추가 정보 표시
            if not args.use_git_date and file_info['git_date']:
                git_date_str = file_info['git_date'].strftime('%Y-%m-%d %H:%M:%S')
                if git_date_str != date_str:
                    print(f"    (Git 커밋: {git_date_str})")
            
            print()


if __name__ == "__main__":
    main()
