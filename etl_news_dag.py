from airflow import DAG
from datetime import datetime
from airflow.operators.empty import EmptyOperator

with DAG(
    "etl_news_dag",
    default_args={"start_date": datetime(2023, 12, 1), "retries": 3},
    schedule_interval="0 3 * * *",
    catchup=False,
) as dag:
    start_task = EmptyOperator(task_id="start_task")

    end_task = EmptyOperator(task_id="end_task")

    start_task >> end_task
