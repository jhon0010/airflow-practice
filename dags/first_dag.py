from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "jhonlotero",
    "retries": 5,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="first_dag_v3",
    description="This is my first DAG",
    default_args=default_args,
    start_date=datetime(2021, 1, 1),
    schedule_interval="@hourly",
) as dag:
    task_1 = BashOperator(
        task_id="task_1", 
        bash_command="echo 'Hello World!'"
        ) 
    task_2 = BashOperator(
        task_id="task_2", 
        bash_command="echo Im a second task :: Hello World!"
        )
    task_3 = BashOperator(
        task_id="task_3", 
        bash_command="echo Im a third task, running same time task2 :: Hello World!"
        )
    

    """
    # method 1 to set the order of the tasks
    task_1.set_downstream(task_2)
    task_1.set_downstream(task_3)

    # method 2 to set the order of the tasks
    task_1 >> task_2
    task_1 >> task_3
    """
    
    # method 3 to set the order of the tasks
    task_1 >> [task_2, task_3]