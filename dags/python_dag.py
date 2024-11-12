from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "jhonlotero",
    "retries": 5,
    "retry_delay": timedelta(minutes=1),
}

def greet(name, age):
    print(f"Hello World from Python Function! {name}, {age}")

with DAG(
    dag_id="first_python_dag_v0",
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
        task_id="task_2", 
        python_callable=lambda: print("Im a second task :: Hello World from Python!")
    )
    task_3 = PythonOperator(
        task_id="task_3", 
        python_callable=greet,
        op_kwargs={"name": "Jhon", "age": 27} # pass the arguments to the function
    )

    # method 3 to set the order of the tasks
    task_1 >> [task_2, task_3]