from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
    "owner": "jhonlotero",
    "retries": 5,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="postgres_v0.12",
    description="This is my postgres DAG",
    default_args=default_args,
    start_date=datetime(2024, 11, 10),
    schedule_interval="0 0 * * *",
    catchup=False,
) as dag:
    create_table_task = PostgresOperator(
        task_id="create_table_task", 
        postgres_conn_id="postgres_conn",
        sql="""
        CREATE TABLE IF NOT EXISTS dag_runs (
            ds VARCHAR NOT NULL,
            dag_id VARCHAR NOT NULL,
            primary key (ds, dag_id)
        );
        """,
        ) 
    
    insert_task = PostgresOperator(
        task_id="insert_task",
        postgres_conn_id="postgres_conn",
        sql="""
        INSERT INTO dag_runs (dt, dag_id)
        VALUES ('{{ ds }}', '{{ dag.dag_id }}');
        """,
    )

    delete_task = PostgresOperator(
        task_id="delete_task",
        postgres_conn_id="postgres_conn",
        sql="""
        DELETE FROM dag_runs WHERE dt = '{{ ds }}' AND dag_id = '{{ dag.dag_id }}';
        """,
    )

    create_table_task >> delete_task >> insert_task