from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator

from tasks.scrapper import scrape
from tasks.save_to_sql import save_to_sql

with DAG(
    "etl_news_dag",
    default_args={"start_date": datetime(2023, 12, 4), "retries": 3},
    schedule_interval="0 3 * * *",
    catchup=False,
) as dag:
    start_task = EmptyOperator(task_id="start_task")

    scrape_the_web = PythonOperator(task_id="scrape", python_callable=scrape)

    to_sql = PythonOperator(task_id="save_to_sql", python_callable=save_to_sql)

    end_task = EmptyOperator(task_id="end_task")

    start_task >> scrape >> save_to_sql >> end_task
