from __future__ import annotations

import ast
import importlib
from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]

SOURCE_FILES = [
    PROJECT_ROOT / "src" / "phone_pipeline" / "ingestion" / "bronze.py",
    PROJECT_ROOT / "src" / "phone_pipeline" / "processing" / "silver.py",
    PROJECT_ROOT / "src" / "phone_pipeline" / "curated" / "gold.py",
    PROJECT_ROOT / "src" / "phone_pipeline" / "utils" / "phone_utils.py",
    PROJECT_ROOT / "src" / "phone_pipeline" / "data_quality" / "validators.py",
    PROJECT_ROOT / "src" / "phone_pipeline" / "data_quality" / "quality_runner.py",
    PROJECT_ROOT / "dags" / "phone_pipeline_dag.py",
]

IMPORTABLE_MODULES = [
    "phone_pipeline.ingestion.bronze",
    "phone_pipeline.processing.silver",
    "phone_pipeline.curated.gold",
    "phone_pipeline.utils.phone_utils",
    "phone_pipeline.data_quality.validators",
    "phone_pipeline.data_quality.quality_runner",
]


@pytest.mark.parametrize("source_path", SOURCE_FILES, ids=lambda path: path.name)
def test_python_files_have_valid_syntax(source_path: Path) -> None:
    source_code = source_path.read_text(encoding="utf-8")
    ast.parse(source_code or "\n", filename=str(source_path))


@pytest.mark.parametrize("module_name", IMPORTABLE_MODULES)
def test_core_modules_are_importable(module_name: str) -> None:
    importlib.import_module(module_name)
