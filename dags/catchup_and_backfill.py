"""
The catchup and backfill feature is used to backfill historical data.
catchup: If you set catchup=True, Airflow will run all the tasks for the start_date and end_date.
backfill: If you set catchup=False, Airflow will only run the tasks that are within the start_date and end_date.
"""

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "jhonlotero",
    "retries": 5,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="catchup_dag_v0",
    description="This DAG has catchup and backfill disabled",
    default_args=default_args,
    start_date=datetime(2024, 11, 10),
    schedule_interval="@hourly",
    catchup=False # when set to True (default value), Airflow will run all the tasks for the start_date and end_date 
) as dag:
    task_1 = BashOperator(
        task_id="task_1", 
        bash_command="echo 'Hello World!'"
        ) 
    
task_1