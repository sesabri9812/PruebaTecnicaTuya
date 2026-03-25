from __future__ import annotations

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_expected_project_files_exist() -> None:
    expected_files = [
        PROJECT_ROOT / "dags" / "phone_pipeline_dag.py",
        PROJECT_ROOT / "data" / "bronze" / "phones_input.json",
        PROJECT_ROOT / "src" / "phone_pipeline" / "ingestion" / "bronze.py",
        PROJECT_ROOT / "src" / "phone_pipeline" / "processing" / "silver.py",
        PROJECT_ROOT / "src" / "phone_pipeline" / "curated" / "gold.py",
        PROJECT_ROOT / "src" / "phone_pipeline" / "utils" / "phone_utils.py",
        PROJECT_ROOT / "src" / "phone_pipeline" / "data_quality" / "validators.py",
        PROJECT_ROOT / "src" / "phone_pipeline" / "data_quality" / "quality_runner.py",
    ]

    missing_files = [str(path.relative_to(PROJECT_ROOT)) for path in expected_files if not path.is_file()]

    assert not missing_files, f"Project is missing expected files: {missing_files}"


def test_expected_data_directories_exist() -> None:
    expected_directories = [
        PROJECT_ROOT / "data" / "bronze",
        PROJECT_ROOT / "data" / "silver",
        PROJECT_ROOT / "data" / "gold",
    ]

    missing_directories = [
        str(path.relative_to(PROJECT_ROOT)) for path in expected_directories if not path.is_dir()
    ]

    assert not missing_directories, f"Project is missing expected directories: {missing_directories}"
