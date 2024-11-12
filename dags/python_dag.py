from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "jhonlotero",
    "retries": 5,
    "retry_delay": timedelta(minutes=1),
}

"""
ti = task instance
"""
def greet(age, ti):
    print(f"Hello World from Python Function! {ti.xcom_pull(task_ids='get_name')}, {age}")

def get_name():
    return "Jhon"

with DAG(
    dag_id="first_python_dag_v2",
    description="This is my first Python DAG",
    default_args=default_args,
    start_date=datetime(2024, 11, 10),
    schedule_interval="@hourly",
) as dag:
    task_1 = PythonOperator(
        task_id="task_1", 
        python_callable=lambda: print("Hello World from Python!")
    )
    task_2 = PythonOperator(
        task_id="get_name", 
        python_callable=get_name
    )
    task_3 = PythonOperator(
        task_id="task_3", 
        python_callable=greet,
        op_kwargs={"age": 27} # pass the arguments to the function
    )

    # 
    task_2 >> [task_1,task_3]