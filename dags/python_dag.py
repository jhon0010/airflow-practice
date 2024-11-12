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
def greet(ti):
    name = ti.xcom_pull(key="name", task_ids=["get_name"])
    last_name = ti.xcom_pull(key="last_name", task_ids=["get_name"])
    age = ti.xcom_pull(key="age", task_ids=["get_age"])
    print(f"Hello {name} {last_name} World from Python Function!, your age is = {age}")

def get_name(ti):
    ti.xcom_push(key="name", value="Jhon")
    ti.xcom_push(key="last_name", value="Lotero")

def get_age(ti):
    ti.xcom_push(key="age", value=27)

with DAG(
    dag_id="first_python_dag_v6",
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
        #op_kwargs={"age": 27} # pass the arguments to the function
    )
    task_4 = PythonOperator(
        task_id="get_age", 
        python_callable=get_age
    )

    [task_2, task_4] >> task_1 >> task_3