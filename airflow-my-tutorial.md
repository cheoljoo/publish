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
    - run 할때 하나 하나 해보는게 실행을 시키면 기본으로 active로 enable 이 된다. 이때 job들이 scheduler에 매우 많이 들어가기에 , 예를 수행해 볼때는 active 되는 것을 off 시키면서 수행을 해주면 하나하나 수행되는 것을 잘 확인할 수가 있다.
    - BashOperator에서 bash_command는 여기에 길게 적어도 되며 , 길경우 변수에 담아서 사용하면 된다.
    - >> 의 변수가 list이면 병렬 처리 이다.
    - branch는 task_id와 return string을 맞추어야 한다.
    - group도 생성할수 있다. 다중 nested 허용
    - subDAG - directory를 따로 만들어 운영 ```import subDags.child_subdag1 as cs1```   ```subdag=cs1.child_subdag1(parent_dag_name=dag_id, child_dag_name="parent_subDAG_sample1")```
      - 모듈화: 큰 DAG를 여러 개의 subDAG으로 나누어 각 subDAG의 기능을 독립적으로 관리할 수 있습니다.
      - 재사용성: 동일한 subDAG를 여러 DAG에서 재사용할 수 있어 코드 중복을 줄일 수 있습니다.
      - 병렬 처리: subDAG는 독립적으로 실행될 수 있어, 전체 DAG의 실행 시간을 단축할 수 있습니다.
      - subDAG를 사용할 때는 주의할 점도 있습니다. 예를 들어, subDAG의 상태가 부모 DAG에 영향을 미칠 수 있으므로, subDAG의 성공 또는 실패가 전체 DAG의 흐름에 미치는 영향을 고려해야 합니다.
    - label 기능
    - TriggerDagRunOperator : 의존 관계를 만들지 않고 , 프로그램상으로 의존성 + 조건에 따른 의존성을 만들기 위해서 사용된다.
      - ```
        # 첫 번째 DAG (first_dag): DummyOperator를 사용하여 시작과 끝을 정의합니다.
        # TriggerDagRunOperator를 사용하여 second_dag를 트리거합니다. 이때 trigger_dag_id 매개변수에 트리거할 DAG의 ID를 지정합니다.
        # conf 매개변수를 통해 추가적인 파라미터를 전달할 수 있습니다. 이 정보는 트리거된 DAG에서 사용할 수 있습니다.
        # 두 번째 DAG (second_dag): 이 DAG은 schedule_interval이 None으로 설정되어 있어, 수동으로만 실행됩니다. 즉, first_dag에서 트리거될 때만 실행됩니다.
        # 사용 시나리오
        # 의존성 관리: first_dag의 작업이 완료된 후 second_dag를 자동으로 실행하여 데이터 파이프라인의 흐름을 관리할 수 있습니다.
        # 조건부 실행: 특정 조건이 충족되었을 때만 second_dag를 실행하도록 설정할 수 있습니다.
        # 이와 같은 방식으로 TriggerDagRunOperator를 활용하여 여러 DAG 간의 연계를 쉽게 관리할 수 있습니다.

        from airflow import DAG
        from airflow.operators.dagrun_operator import TriggerDagRunOperator
        from airflow.operators.dummy_operator import DummyOperator
        from datetime import datetime

        # 첫 번째 DAG 정의
        with DAG('first_dag',
                schedule_interval='@daily',
                start_date=datetime(2023, 11, 1),
                catchup=False) as dag1:

            start = DummyOperator(task_id='start')

            trigger_second_dag = TriggerDagRunOperator(
                task_id='trigger_second_dag',
                trigger_dag_id='second_dag',  # 트리거할 DAG의 ID
                conf={"key": "value"},  # 추가적인 파라미터
                dag=dag1
            )

            end = DummyOperator(task_id='end')

            start >> trigger_second_dag >> end

        # 두 번째 DAG 정의
        with DAG('second_dag',
                schedule_interval=None,  # 수동으로 트리거되므로 None
                start_date=datetime(2023, 11, 1),
                catchup=False) as dag2:

            start_second = DummyOperator(task_id='start_second')

            end_second = DummyOperator(task_id='end_second')

            start_second >> end_second
        ```
    - ExternalTaskSensor를 사용하면 여러 DAG 간의 의존성을 쉽게 관리할 수 있습니다.
      - ExternalTaskSensor는 Apache Airflow에서 사용되는 센서 중 하나로, 특정 외부 작업이 완료되었는지를 감지하는 데 사용됩니다. 이 센서는 다른 DAG(Directed Acyclic Graph)에서 실행된 작업의 상태를 확인하고, 해당 작업이 성공적으로 완료되면 다음 작업을 실행하도록 트리거합니다.
    - xcom으로 task간 데이터 전달
    - task간 json data 전달
      - ```
        # DAG 정의: DAG 객체를 생성하고, 시작 날짜와 스케줄을 설정합니다.
        # JSON 데이터 푸시: push_json_data 함수는 JSON 데이터를 생성하고, xcom_push 메서드를 사용하여 XCom에 데이터를 푸시합니다. kwargs['ti']는 태스크 인스턴스를 참조합니다.
        # JSON 데이터 풀기: pull_json_data 함수는 xcom_pull 메서드를 사용하여 이전 태스크에서 푸시한 JSON 데이터를 가져옵니다. 가져온 데이터는 콘솔에 출력됩니다.
        # 태스크 의존성 설정: push_task가 완료된 후에 pull_task가 실행되도록 의존성을 설정합니다.
        from airflow import DAG
        from airflow.operators.python_operator import PythonOperator
        from datetime import datetime

        # JSON 데이터를 생성하는 함수
        def push_json_data(**kwargs):
            json_data = {
                "id": 1,
                "name": "Alice",
                "email": "alice@example.com"
            }
            # XCom에 JSON 데이터 푸시
            kwargs['ti'].xcom_push(key='user_data', value=json_data)

        # JSON 데이터를 가져오는 함수
        def pull_json_data(**kwargs):
            # XCom에서 JSON 데이터 가져오기
            ti = kwargs['ti']
            json_data = ti.xcom_pull(task_ids='push_task', key='user_data')
            print(f"Retrieved JSON data: {json_data}")

        # DAG 정의
        with DAG('json_data_transfer_dag',
                start_date=datetime(2023, 11, 25),
                schedule_interval='@daily',
                catchup=False) as dag:

            # JSON 데이터를 푸시하는 태스크
            push_task = PythonOperator(
                task_id='push_task',
                python_callable=push_json_data,
                provide_context=True
            )

            # JSON 데이터를 풀어오는 태스크
            pull_task = PythonOperator(
                task_id='pull_task',
                python_callable=pull_json_data,
                provide_context=True
            )

            # 태스크 의존성 설정
            push_task >> pull_task
        ```
    - DAG객체 안에 user_defined_macros를 설정하면 Task에서 JinjaTemplate으로 불러 사용가능하다.
      - MACRO_VARS={     "id" : "sampleID",     "pw" : 1234,     "dataset" : "userDS" }
    - error 발생시 : success가 아닌 결과가 나타남.
      - Graph에서 박스를 누그로 Log를 선택하며 보면 console log를 볼수 있음.
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

# Airflow 외부 python 함수 수행하기
- common 한 것들을 plugins/common/*.py로 모아두고 사용하고 싶을때 [Link](https://letzgorats.tistory.com/entry/Airflow-%EC%99%B8%EB%B6%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%95%A8%EC%88%98-%EC%88%98%ED%96%89%ED%95%98%EA%B8%B0)
- code 안에서는 ```from common.common_func import get_A``` 선언하고 사용할때 문제가 없으려면
  - .env 안에 다음을 선언해야 한다.
    - WORKSPACE_FOLDER=..../airflow
    - PYTHONPATH=${WORKSPACE_FOLDER}/plugins


# 분산 환경
- 실제로 사용하려면 분산 환경에서 일을 주고 받을 수 있어야 할 것이다. 분산 환경에서 일을 할당하며 관리하는 것에 대해서 알아볼 것이다.
  - https://airflow.apache.org/docs/apache-airflow/stable/index.html
  - https://louisdev.tistory.com/3


# 기타
- >> operation overloading
  - https://github.com/cheoljoo/publish/blob/main/airflow_operator_overloading.md
- TaskFlow API : 새로운 문법으로 Airflow DAG 생성하기
  - https://phi-friday.github.io/@post/python/airflow1/
- email operator
  - https://letzgorats.tistory.com/entry/Airflow-Email-Operator%EB%A1%9C-%EB%A9%94%EC%9D%BC-%EC%A0%84%EC%86%A1%ED%95%98%EA%B8%B0
  - I failed to do it with email operator in my company instead of gmail.
- Airflow - DAG workflow 작성 / 실행 / 이해 
  - https://da2so.tistory.com/40