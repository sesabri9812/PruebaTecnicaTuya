from __future__ import annotations

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DAG_PATH = PROJECT_ROOT / "dags" / "phone_pipeline_dag.py"


def test_dag_file_exists() -> None:
    assert DAG_PATH.is_file(), "The DAG file should exist in the dags directory"


def test_dag_file_has_python_extension() -> None:
    assert DAG_PATH.suffix == ".py"
