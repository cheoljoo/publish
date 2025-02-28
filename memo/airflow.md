- description : airflow 관련 내용을 정리해두는 페이지이다.
- tag : airflow , etl
- date : 2025-01-01

# ETL (Extract,Transforming,Load)
- airflow
  - airflow 를 추천하시는 이유는 python 사용할수 있기 때문인가요? airflow와 같은 ETL (extract , transform , Load) 을 사용하시려는 이유는 무엇인가요? TAF에 이것을 적용하면 , flow도 더 쉽게 확인할수 있겠다는거죠.. 특히 , 같이 python이니 코드 재사용도 가능하고.. 맞나요?
    1. airflow  이 좋을 것 같은 이유는   VS code 처럼 platform (규격) 화 되어 있고  유용한 application 이 많아서  입니다.
     물론 ptyhon 코드화 된것도  끌리는 이유중 하나 입니다.
    1.   flow 확인과 더불어  현재 TAF system 에서 할 수 없는  backfill   기능이 되기 때문입니다.
    - Backfill이 쉬움: Backfill이라고 하면 실패한 데이터 파이프라인을 재실행하는 것을 의미합니다. Airflow는 task가 실패해도 그 결과 기록을 잘 남기고 원하는 시점에 맞게 재실행을 쉽게할 수 있도록 지원합니다.
  - https://velog.io/@clueless_coder/Airflow-%EC%97%84%EC%B2%AD-%EC%9E%90%EC%84%B8%ED%95%9C-%ED%8A%9C%ED%86%A0%EB%A6%AC%EC%96%BC-%EC%99%95%EC%B4%88%EC%8B%AC%EC%9E%90%EC%9A%A9
  - [Airflow-개발환경-셋팅하기-on-Docker](https://velog.io/@jskim/Airflow-%EA%B0%9C%EB%B0%9C%ED%99%98%EA%B2%BD-%EC%85%8B%ED%8C%85%ED%95%98%EA%B8%B0-on-Docker)