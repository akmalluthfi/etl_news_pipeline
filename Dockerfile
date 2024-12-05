FROM apache/airflow:2.10.3-python3.9
USER airflow
WORKDIR /opt/airflow/dags

COPY etl_news_dag.py .
COPY tasks/ ./tasks

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080