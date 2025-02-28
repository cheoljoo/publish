- description : python에서 Popen (process run)을 사용할때의 주의점
- tag : python , Popen , subprocess
- date : 2025-01-01

# chatgpt answer

- we print the binary data into console. At that time , we can meet the following error.
- we need to use subprocess.Popen instead of os.popen
```
console = os.popen('cd {dir}; echo -n "<<gitbranch>>"; git branch --show-current; echo "  "; echo -n "<<gitremote>>"; git remote -v ; echo "<<gitblame>>"; git blame -f -e -w {file}'.format(dir=csvfile['dir'],file=csvfile['file'])).read()
    File "/usr/lib/python3.8/codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xa0 in position 10804: invalid start byte
````

to

```
import subprocess

command = 'cd {dir}; echo -n "<<gitbranch>>"; git branch --show-current; echo "  "; echo -n "<<gitremote>>"; git remote -v; echo "<<gitblame>>"; git blame -f -e -w {file}'.format(dir=csvfile['dir'],file=csvfile['file'])
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, encoding='utf-8', errors='ignore')
output, error = process.communicate()

if error:
    print("Error:", error)

console = output
```