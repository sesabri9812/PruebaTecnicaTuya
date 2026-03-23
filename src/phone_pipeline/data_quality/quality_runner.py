from __future__ import annotations

from typing import Any

from phone_pipeline.data_quality.validators import validate_bronze_records
from phone_pipeline.ingestion.bronze import load_bronze_data


def run_data_quality_checks(records: list[dict[str, Any]]) -> dict[str, Any]:
    validation_results = validate_bronze_records(records)
    failed_rows = [result for result in validation_results if result["errors"]]

    return {
        "total_rows": len(records),
        "failed_rows": len(failed_rows),
        "passed_rows": len(records) - len(failed_rows),
        "results": validation_results,
    }


def run_bronze_quality_checks() -> dict[str, Any]:
    return run_data_quality_checks(load_bronze_data())


def run_quality_checks(records: list[dict[str, Any]]) -> dict[str, Any]:
    return run_data_quality_checks(records)
