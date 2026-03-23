from __future__ import annotations

try:
    from airflow import DAG
    from airflow.operators.python import PythonOperator
except ImportError:  # pragma: no cover
    DAG = None
    PythonOperator = None

from phone_pipeline.curated.gold import run_gold_pipeline
from phone_pipeline.data_quality.quality_runner import run_bronze_quality_checks
from phone_pipeline.processing.silver import build_silver_dataset


def create_phone_pipeline_dag():
    if DAG is None or PythonOperator is None:
        return None

    with DAG(
        dag_id="phone_pipeline",
        schedule="@daily",
        catchup=False,
    ) as dag:
        quality_task = PythonOperator(
            task_id="run_bronze_quality_checks",
            python_callable=run_bronze_quality_checks,
        )
        silver_task = PythonOperator(
            task_id="build_silver_dataset",
            python_callable=build_silver_dataset,
        )
        gold_task = PythonOperator(
            task_id="run_gold_pipeline",
            python_callable=run_gold_pipeline,
        )

        quality_task >> silver_task >> gold_task
        return dag


dag = create_phone_pipeline_dag()
