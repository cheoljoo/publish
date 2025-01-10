TOC
- [1. python](#1-python)
  - [1.1. import logging](#11-import-logging)
  - [1.2. loguru](#12-loguru)
    - [1.2.1. loguru를 이용한 logger 사용 (class 이름 포함)](#121-loguru를-이용한-logger-사용-class-이름-포함)
      - [1.2.1.1. metaclass 이용](#1211-metaclass-이용)
        - [1.2.1.1.1. hello.py](#12111-hellopy)
        - [1.2.1.1.2. logger\_meta.py](#12112-logger_metapy)
        - [1.2.1.1.3. logger\_config.py](#12113-logger_configpy)
        - [1.2.1.1.4. print result](#12114-print-result)
      - [1.2.1.2. decorator 이용한 방법](#1212-decorator-이용한-방법)
        - [1.2.1.2.1. hello3.py](#12121-hello3py)
        - [1.2.1.2.2. logger\_decorator.py](#12122-logger_decoratorpy)
  - [1.3. Q\&A](#13-qa)
- [2. bash](#2-bash)
- [3. 슬기롭게 로그(log) 쌓는 법](#3-슬기롭게-로그log-쌓는-법)
  - [3.1. log format을 무엇으로 하는 것이 좋을까?](#31-log-format을-무엇으로-하는-것이-좋을까)
- [4. Reference](#4-reference)

-------------------

# 1. python
## 1.1. import logging
- Python’s standard library
- 기본 설정
  - ```python
    # 로그 설정
    logging.basicConfig(
        level=logging.INFO,        # 로그 레벨 (INFO 이상)
        format='%(asctime)s - %(levelname)s - %(message)s',  # 로그 출력 포맷
        datefmt='%Y-%m-%d %H:%M:%S'  # 날짜 포맷
    )
    # 로거 생성
    logger = logging.getLogger('my_logger')  # (__name__)  __name__ is instantiating your logger
    ```
- logging to a file
  - ```python
    logging.basicConfig(
        filename="app.log",
        encoding="utf-8",
        filemode="a",
     ```
- Displaying Variable Data
  - ```logging.debug(f"{name=}")```  -> 2024-07-22 14:49 - DEBUG - name='Samara'
- Capturing Stack Traces : exc_info=True  or logging.exception("DonutCalculationError")
  - ```python
    try:
        donuts_per_guest = donuts / guests
    except ZeroDivisionError:
        logging.error("DonutCalculationError", exc_info=True)
    ```
- Using Handlers (당신이 추가하고 싶은 것을 마음대로)
  - ```python
    import logging
    logger = logging.getLogger(__name__)
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler("app.log", mode="a", encoding="utf-8")
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.handlers
    ```
  - result : ```[ <StreamHandler <stderr> (NOTSET)>,  <FileHandler /Users/RealPython/Desktop/app.log (NOTSET)>  ]```   NOTSET : log level is not set yet.
- ```logger.setLevel("WARNING")```
- Filtering Logs
  - ```python
    def show_only_debug(record):
        return record.levelname == "DEBUG"
    console_handler.addFilter(show_only_debug)
    ```

| Log Level  | Function               | Description                                               |
|------------|------------------------|-----------------------------------------------------------|
| DEBUG      | logging.debug()        | Provides detailed information that’s valuable to you as a developer. |
| INFO       | logging.info()         | Provides general information about what’s going on with your program. |
| WARNING     | logging.warning()      | Indicates that there’s something you should look into.   |
| ERROR      | logging.error()        | Alerts you to an unexpected problem that’s occurred in your program. |
| CRITICAL   | logging.critical()     | Tells you that a serious error has occurred and may have crashed your app. |


## 1.2. loguru
- pip3 install loguru
- ```python
  from loguru import logger

  logger.trace("This is a trace message.")
  logger.debug("This is a debug message")
  logger.info("This is an info message.")
  logger.success("This is a success message.")
  logger.warning("This is a warning message.")
  logger.error("This is an error message.")
  logger.critical("This is a critical message.")
  ```
  - result has colorful text. it is better than standard library of python.
- 여기서 trace level을 볼수 없다. 다음과 같이 하면 trace level도 stdout으로 나오게 된다.
  - ```python
    from loguru import logger
    import sys        # <!- add this line

    logger.remove(0)             # <- add this line
    logger.add(sys.stdout, level="TRACE")   # <- add this line

    logger.trace("This is a trace message.")
    ...
    ```
- logging with json : add serialize option to the add()
- ```python
  logger.remove(0)
  logger.add(sys.stderr, serialize=True) # <- add this line
  logger.error("This is  an error message.")
  ```
  - output
    - ```python
      {"text": "2023-03-28 09:36:31.458 | ERROR    | __main__:<module>:7 - This is  an error message.\n", "record": {"elapsed": {"repr": "0:00:00.023078", "seconds": 0.023078}, "exception": null, "extra": {}, "file": {"name": "loguru_demo.py", "path": "/home/<your_username/loguru_demo/loguru_demo.py"}, "function": "<module>", "level": {"icon": "❌", "name": "ERROR", "no": 40}, "line": 7, "message": "This is  an error message.", "module": "loguru_demo", "name": "__main__", "process": {"id": 25826, "name": "MainProcess"}, "thread": {"id": 140082527805440, "name": "MainThread"}, "time": {"repr": "2023-03-28 09:36:31.458896+02:00", "timestamp": 1679988991.458896}}}
      ```
  - cherry pick the fields
    - ```python
      import json     # <!- add this line

      # Add the following function
      def serialize(record):
          subset = {
                  "level": record["level"].name,
                  "timestamp": record["time"].timestamp(),
                  "message": record["message"]}
          return json.dumps(subset)

      # Add the following function
      def formatter(record):
          record["extra"]["serialized"] = serialize(record)
          return "{extra[serialized]}\n"

      logger.remove(0)
      logger.add(sys.stderr, format=formatter)   # <!-

      logger.error("This is  an error message.")
      ```
- write log to file
  - ```python
    from loguru import logger

    logger.remove(0)
    '''modify the following line'''
    logger.add("app.log", format="{level} : {time} : {message}: {process}")
    logger.error("This is  an error message.")
    ```

### 1.2.1. loguru를 이용한 logger 사용 (class 이름 포함)
#### 1.2.1.1. metaclass 이용
- ```logger = configure_logger(classname='__main__')```
- class Hello(```metaclass=LoggerMeta```)
- ```self.logger```.info("hello world: {}", self.temp)
##### 1.2.1.1.1. hello.py
```python
# hello.py
from loguru import logger
import sys
from logger_meta import LoggerMeta  # LoggerMeta 모듈 import
from logger_config import configure_logger

# 로거 설정
#logger.remove()  # 기본 핸들러 제거
#fmt = "{time} | {level} | {extra[classname]}:{function}:{line} - {message}"
#logger.add(sys.stdout, format=fmt)

logger = configure_logger(classname='__main__')

class Hello(metaclass=LoggerMeta):
    def __init__(self):
        self.temp = 'AAAA'  # 추가적인 속성 초기화

    def world(self):
        self.logger.info("hello world: {}", self.temp)  # temp 속성 사용

def print_logger_test():
    logger.info('this is local function test')

# 사용 예
if __name__ == "__main__":
    hello_instance = Hello()
    hello_instance.world()
    logger.info('main world: {}')
    print_logger_test()

```
##### 1.2.1.1.2. logger_meta.py
- self.logger에 각 class마다 자신의 이름을 classname에 각인
```python
# logger_meta.py
from loguru import logger

class LoggerMeta(type):
    def __new__(cls, name, bases, attrs):
        cls_instance = super().__new__(cls, name, bases, attrs)
        cls_instance.logger = logger.bind(classname=name)
        return cls_instance
```
##### 1.2.1.1.3. logger_config.py
- class가 아닌 __main__ 영역에서의 logger 사용
```python
# logger_config.py
from loguru import logger
import sys

def configure_logger(classname='__main__'):
    logger.remove()  # Remove default handlers
    fmt = "{time} | {level} | {extra[classname]}:{function}:{line} - {message}"
    logger.add(sys.stdout, format=fmt)
    return logger.bind(classname=classname)

```
##### 1.2.1.1.4. print result
```txt
2025-01-10T08:59:07.282312+0900 | INFO | Hello:world:19 - hello world: AAAA
2025-01-10T08:59:07.282433+0900 | INFO | __main__:<module>:28 - main world: {}
2025-01-10T08:59:07.282538+0900 | INFO | __main__:print_logger_test:22 - this is local function test
```
#### 1.2.1.2. decorator 이용한 방법
- ```@logger_bind```
- ```self.logger```.info("hello world: {}", self.temp)
##### 1.2.1.2.1. hello3.py
```python
# main.py
from loguru import logger
from logger_decorator import logger_bind
import logging

# 로그 포맷 설정 : if you want to change format (ex. add filename)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s     | %(filename)s:%(lineno)d:%(name)s:%(funcName)s - %(message)s'
)
logger = logging.getLogger()

@logger_bind
class Hello:
    def __init__(self):
        self.temp = 'AAA'

    def world(self):
        self.logger.info("hello world: {}".format(self.temp))

def print_test():
    logger.info('example of test')

# Example usage
if __name__ == "__main__":
    logger.info("main world: {}")

    hello_instance = Hello()
    hello_instance.world()

    logger.info("main world: {}")
    print_test()
```
##### 1.2.1.2.2. logger_decorator.py
```python
# logger_decorator.py
import logging
from functools import wraps

def logger_bind(cls):
    # Create a logger for the class
    logger = logging.getLogger(cls.__name__)
    logger.setLevel(logging.INFO)

    # Create a console handler and set level to info
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # "{time} | {level} | {extra[classname]}:{function}:{line} - {message}"
    formatter = logging.Formatter('%(asctime)s | %(levelname)s     | %(filename)s:%(lineno)d:%(name)s:%(funcName)s - %(message)s')
    ch.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(ch)

    # Bind the logger to the class
    cls.logger = logger
    return cls
```

## 1.3. Q&A
- [how to log hte class of a method](https://github.com/Delgan/loguru/issues/430)

# 2. bash
- 이미 작성된 파일의 규칙을 잘 지키는 것이 중요!  $? 의 값을 꼭 확인하면 좋을 것이고, bash용 open source log library를 사용하면 좋을 듯
  - [bashlog](https://github.com/Zordrak/bashlog) : star 80 : fork 21
    - ```set -uo pipefail;``` 을 사용
    - ```bash
      log info 'My info message';
      log warn 'My warning message';
      log error 'My error message';
      log debug 'My debugging message';
      ```
    - Bash Debug Trap
      - ```bash
        my_command --with very -c -o -m -p -l -e -x -- parameters \
          && log debug "${prev_cmd}" \
          || log error "${prev_cmd};
        ```
  - [bash logger](https://github.com/adoyle-h/bash-logger) : star 12 : fork 3
    - ```bash
      # file: ./test/logger.sh
      # import the logger script
      source "<path>/logger.sh ""

      function foo() {
          ENTER
          DEBUG "DEBUG message"
          INFO "INFO message"
          echo "echo message"
          WARN "WARN message"
          ERROR "ERROR message"
          EXIT
      }

      ENTER

      foo

      EXIT
      ```
    - results
      - ```txt
        [2017/06/30 15:36:07][DEBUG](ENTER) script: ./test/logger.sh
        [2017/06/30 15:36:07][DEBUG](ENTER) function: foo
        [2017/06/30 15:36:07][DEBUG](foo) DEBUG message
        [2017/06/30 15:36:07][INFO](foo) INFO message
        echo message
        [2017/06/30 15:36:07][WARN](foo) WARN message
        [2017/06/30 15:36:07][ERROR](foo) ERROR message
        [2017/06/30 15:36:07][DEBUG](EXIT) function: foo
        [2017/06/30 15:36:07][DEBUG](EXIT) script: ./test/logger.sh
        ```
- file name , file line , func name 의 내용을 같이 print해주면 좋을 듯!
  - ```bash
    my_function() {
        echo "Function name: ${FUNCNAME[0]}"
        echo "File name: ${BASH_SOURCE[0]}"
        echo "Line number: ${LINENO}"
    }
    ```
- [x-trace](https://www.baeldung.com/linux/logging-bash-scripts)
  - The option set -x starts printing each command, while set +x stops this behavior.
- 


# 3. [슬기롭게 로그(log) 쌓는 법](https://simplifyprocess.tistory.com/13)
- 코드 위치 기반 로깅 -> 시간 , 함수 , 내용....
- 기능 문맥 기반 로깅 -> 내용 부분에 기능 적인 부분이 추가 됨.
* 2가지를 합쳐서 사용하면 될 듯
## 3.1. log format을 무엇으로 하는 것이 좋을까?
- 시간 : level : process : file : # : class : function : message
- 개발자들만의 자체 룰은?
  - 없으면 만들어서 고쳐가야 한다.

# 4. Reference
- [python logger](https://coldbrown.co.kr/2023/07/python-19-%EB%A1%9C%EA%B7%B8logging%EB%A5%BC-%EB%82%A8%EA%B8%B0%EB%8A%94-%EB%B0%A9%EB%B2%95/)
- [realpython](https://realpython.com/python-logging/)
- [The 5 Best Logging Libraries for Python](https://www.highlight.io/blog/5-best-python-logging-libraries)
