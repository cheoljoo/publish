# Airflow의 `>>` 연산자 구현 : operator overloading

- Apache Airflow에서 `>>` 연산자는 **연산자(Task)의 순서를 정의**하기 위한 특별한 문법으로, Python의 **연산자 오버로딩**을 사용해 구현되어 있습니다. 

---

## 1. `>>` 연산자의 구현

### `BaseOperator` 클래스의 `__rshift__` 메서드
`>>` 연산자는 Python의 `__rshift__` 메서드를 통해 구현됩니다. 

```python
class BaseOperator:
    ...
    def __rshift__(self, other):
        """Implements task1 >> task2 functionality."""
        self.set_downstream(other)
        return other
```
  - self: >> 연산자 왼쪽에 있는 Task (task1).
  - other: >> 연산자 오른쪽에 있는 Task (task2).
  - set_downstream(other): task1을 선행 작업, task2를 후속 작업으로 DAG에 연결.
  - 마지막으로 other를 반환하여 연쇄적인 작업 정의가 가능합니다 (예: task1 >> task2 >> task3).

```python
class BaseOperator:
    ...
    def set_downstream(self, task_or_task_list):
        """Sets the downstream dependencies for this task."""
        if isinstance(task_or_task_list, list):
            for task in task_or_task_list:
                self._add_edge(self, task)
        else:
            self._add_edge(self, task_or_task_list)

    def _add_edge(self, upstream_task, downstream_task):
        """Adds an edge between two tasks in the DAG."""
        self.dag.add_edge(upstream_task, downstream_task)
```
  - set_downstream(task_or_task_list): 하나의 Task 또는 Task 목록을 받아, 종속성을 설정.
  - _add_edge(upstream_task, downstream_task): DAG 객체에 선행 작업과 후속 작업 간의 연결 정보를 추가.

### 실행 흐름 요약
- DAG Trigger: 스케줄 또는 수동 실행으로 DagRun 생성.
- Scheduler:
  - DAG의 Task 간 종속성을 분석.
  - 실행 가능한 Task를 큐에 추가.
- Worker: 큐에서 Task를 가져와 실행.
- Task 실행 완료:
  - 성공 시: 상태가 success로 업데이트되고, 후속 작업 실행.
  - 실패 시: 재시도 또는 failed 상태로 종료.


