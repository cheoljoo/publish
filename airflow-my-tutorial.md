# How to run with airflow docker
- [Airflow docker-compose로 에어플로우 설치하기](https://velog.io/@sophi_e/Airflow-docker-compose%EB%A1%9C-%EC%97%90%EC%96%B4%ED%94%8C%EB%A1%9C%EC%9A%B0-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0)
  - i will try to do with docker. because my system does not work well with ```pip3 install apache-airflow```
- 보석 공장을 예시로 든 이유가 있는데, 에어플로우는 실시간으로, 초단위로 진행되어야 하는 공정에는 적합하지 않다. 보석 공장처럼 하루 한 번, 일주일에 한 번 이렇게 진행되는 공정을 관리하는 데에 적합하다.
- change port : flower 5555 -> 5559 , web 8080 -> 5558 in docker-compose.yaml
  ```
  airflow-webserver:
      <<: *airflow-common
      command: webserver
      ports:
        - 5558:8080
      healthcheck:
        test: ["CMD", "curl", "--fail", "http://localhost:5558/health"]
   flower:
      <<: *airflow-common
      command: celery flower
      profiles:
        - flower
      ports:
        - 5559:5555
      healthcheck:
        test: ["CMD", "curl", "--fail", "http://localhost:5559/"]
  ```
- version 1 : ```docker-compose --profile flower up```
- version 2 : ```docker compose --profile flower up``` <- we need to do
  - ```--profile flower```은 환경을 모니터링하는 option임 http://localhost:5559
  - ```~/airflow  $  docker compose up airflow-init```
- account : airflow / airflow
- https://airflow.apache.org/docs/apache-airflow/2.5.1/docker-compose.yaml 파일 안에  build: . 을 활성화한후에 FROM apache/airflow:2.5.1-python3.8 RUN pip install airflow-code-editor 을 추가하려 한다. yaml의 어느 부분에 추가를 해야 하는가?
  - Dockerfile 추가 docker-compose.yaml 파일과 동일한 디렉토리에 Dockerfile을 생성하여
    - FROM apache/airflow:2.5.1-python3.8
    - RUN pip install airflow-code-editor
  - 이후 ```docker compose build```   / ```docker compose up```
- docker compose up 을 damon으로 수행시키고 싶으면?  -->   ```docker compose up -d```
  - 컨테이너 로그 확인: ```docker compose logs -f```
    - ```-f``` 옵션은 실시간 로그 스트리밍을 활성화합니다.
  - 모든 컨테이너 중지 및 정리: ```docker compose down```

# How to use 
- [Airflow 엄청 자세한 튜토리얼 #왕초심자용](https://velog.io/@clueless_coder/Airflow-%EC%97%84%EC%B2%AD-%EC%9E%90%EC%84%B8%ED%95%9C-%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC-%EC%99%95%EC%B4%88%EC%8B%AC%EC%9E%90%EC%9A%A9)
  - it gave good explanation. but , naver_search_pipeline.py is not working.
  - it has the following error although i add preprocess python package in Dockerfile for naver_search_pipeline.py.
    - ```
      Broken DAG: [/opt/airflow/dags/naver_search_pipeline.py] Traceback (most recent call last):
        File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
        File "/opt/airflow/dags/naver_search_pipeline.py", line 5, in <module>
          from preprocess.naver_preprocess import preprocessing
      ModuleNotFoundError: No module named 'preprocess.naver_preprocess'; 'preprocess' is not a package
      ```
  - 웹서버 사용하기
    - 예시 DAG : example_branch_datetime_operator_2
- [>> operator overloading 설명 in airflow](https://github.com/cheoljoo/publish/blob/main/airflow_operator_overloading.md)
- DAG 만들기
  - [가장 기본 DAG 만들어 실행해보기](https://magpienote.tistory.com/196)  <- [Example Source](https://github.com/hyunseokjoo/airflow_sample_code)
    - list에 들어간 것은 병렬 처리
  - success / failure 처리 (return or exception or exit)
    - Bash에서 exit 코드에 따른 동작
      - exit 0: 성공 상태(success), DAG 흐름이 계속됨.
      - exit != 0: 실패 상태(failed), DAG 흐름이 중단되거나 재시도.
    - Python에서 에러 처리
      - raise Exception: Task가 실패로 기록되고 이후 실행이 중단.
      - 조건 처리와 예외 발생을 통해 실패 조건을 명확히 정의 가능.
    - How BranchPythonOperator Works
      - Task Completion: The BranchPythonOperator itself is marked as successful (success) if the Python callable executes without raising an exception. If an exception occurs in the callable, the task is marked as failed (failed), and the DAG's execution flow stops or retries based on your configuration.
      - Return Value Determines Next Task(s): The return value of the callable is a **task ID** (or list of task IDs) that the BranchPythonOperator will trigger as the next step. Tasks not returned are automatically skipped.
      - ```python
        from airflow import DAG
        from airflow.operators.python import BranchPythonOperator
        from airflow.operators.dummy_operator import DummyOperator
        from datetime import datetime
        
        def decide_branch():
            # Logic to decide the branch
            value = 1
            if value == 1:
                return "task_true"    # it runs task with (task_id="task_true")
            else:
                return "task_false"   # it runs task with (task_id="task_false"). return string == task_id
        
        with DAG(
            dag_id="branch_example",
            start_date=datetime(2023, 1, 1),
            schedule_interval=None,
            catchup=False,
        ) as dag:
            start = DummyOperator(task_id="start")
        
            branch = BranchPythonOperator(
                task_id="branch",
                python_callable=decide_branch
            )
        
            task_true = DummyOperator(task_id="task_true")
            task_false = DummyOperator(task_id="task_false")
            end = DummyOperator(task_id="end")
        
            start >> branch >> [task_true, task_false]
            [task_true, task_false] >> end
        ```
