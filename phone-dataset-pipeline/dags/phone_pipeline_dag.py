from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from phone_pipeline.processing.gold import run_gold_pipeline


def execute_gold():
    result = run_gold_pipeline()

    print("=== TABLE ===")
    print(result["table"][:5])

    print("=== METRICS ===")
    print(result["metrics"])


default_args = {
    "owner": "data-engineer",
    "retries": 1,
}

with DAG(
    dag_id="gold_phone_pipeline",
    default_args=default_args,
    description="Pipeline GOLD de teléfonos",
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    run_gold_task = PythonOperator(
        task_id="run_gold_pipeline",
        python_callable=execute_gold,
    )

    run_gold_task