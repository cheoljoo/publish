- description : bash scripts 모음
- tag : bash , scripts
- date : 2023-01-01

TOC
- [1. who uses the most file size?](#1-who-uses-the-most-file-size)
- [2.](#2)


-------------------

# 1. who uses the most file size?
- (chatgpt) requirement : To create a shell script that captures the results of the find command into a variable and then performs operations on the found directories, you need to use a loop to iterate over each result.
- aloga.sh
```bash
#!/bin/bash

# Find directories named 'ALOGA'
found_dirs=$(find . -type d -name 'ALOGA' 2>/dev/null)

# Check if any directories were found
if [ -z "$found_dirs" ]; then
    echo "No directories named 'ALOGA' found."
    exit 1
fi

# Iterate over each found directory
for dir in $found_dirs; do
    echo "==== [ $dir ] ===="

    # sort
        du -sh  ${dir}/*  | sort -rh
done

#echo "==== [ Disk Usage ] ===="
#for dir in $found_dirs; do
#du -sh "$dir"
#done

echo "==== [ Sorted Disk Usage ] ===="
du -sh $found_dirs | sort -rh

```

# 2. 