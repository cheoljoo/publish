- description : 한글이 들어간 path가 unicode로보일때 이를 decode하는 코드이다. git status를 하면 한글이 보이지 않게 된다. 
- tag : unicode , encode , decode , hangul,korean-lang
- date : 2025-03-06

# git status 가 다음같이 보일때
- ```txt
  $ git status
  On branch main
  Your branch is up to date with 'origin/main'.
  
  Changes not staged for commit:
    (use "git add <file>..." to update what will be committed)
    (use "git restore <file>..." to discard changes in working directory)
        modified:   "education/react-\354\231\204\353\262\275-\352\260\200\354\235\264\353\223\234-2025-with-react-router--redux/index.md"
        modified:   "education/\354\227\205\353\254\264-\355\232\250\354\234\250\354\235\204-\355\231\225-\353\201\214\354\226\264\354\230\254\353\246\254\353\212\224-GitHub-Copilot\355\231\234\354\232\251-\355\224\204\353\241\234\352\267\270\353\236\230\353\260\215/index.md"
```
- 다음 한글을 읽을수 없다. 이는 open을 할때도 error 가 발생한다. 

# solution
- I can not explain why this code is working well.
- ```python
  decoded_string = decoded_string.encode('latin1').decode('unicode_escape')
  decoded_string = decoded_string.encode('latin1').decode('utf-8')
  ```

- test code
    - ```python
      import re
      decoded_string = "education/react-\354\231\204\353\262\275-\352\260\200\354\235\264\353\223\234-2025-with-react-router--redux/index.md"
      #print(decoded_string)
      #decoded_string = re.sub(r'\\\\', r'\\', decoded_string)
      #print(decoded_string)
      decoded_string = decoded_string.encode('latin1').decode('utf-8')
      print(decoded_string)
      
      decoded_string = 'education/react-\\354\\231\\204\\353\\262\\275-\\352\\260\\200\\354\\235\\264\\353\\223\\234-2025-with-react-router--redux/index.md'
      #print(decoded_string)
      #decoded_string = re.sub(r'\\\\', r'\\', decoded_string)
      #print(decoded_string)
      decoded_string = decoded_string.encode('latin1').decode('unicode_escape')
      decoded_string = decoded_string.encode('latin1').decode('utf-8')
      print(decoded_string)
      ```



