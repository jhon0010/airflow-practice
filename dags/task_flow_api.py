from datetime import datetime, timedelta

from airflow.decorators import dag, task

default_args = {
    "owner": "jhonlotero",
    "retries": 5,
    "retry_delay": timedelta(minutes=1),
}

@dag(
    dag_id="dataflow_etl_v0.3",
    description="This is my first Python DAG",
    default_args=default_args,
    start_date=datetime(2024, 11, 10),
    schedule_interval="@daily",
)
def dataflow_etl():

    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name': 'Jhon',
            'last_name': 'Lotero'
        }

    @task()
    def get_age():
        return  27

    @task()
    def greet(first_name, last_name, age):
        print(f"Hello {first_name} {last_name} World from Python Function!, your age is = {age}")

    dict_names = get_name()
    age = get_age()
    greet(first_name=dict_names['first_name'],last_name=dict_names['last_name'] ,age=age)

dataflow_etl_dag = dataflow_etl()