from __future__ import annotations

from phone_pipeline.data_quality.quality_runner import run_bronze_quality_checks, run_data_quality_checks
from phone_pipeline.data_quality.validators import validate_bronze_records, validate_required_fields


def test_validate_required_fields_reports_missing_values() -> None:
    errors = validate_required_fields({"customer_id": "", "phone": "3001234567"})

    assert "Missing required field: customer_id" in errors
    assert "Missing required field: source" in errors


def test_validate_bronze_records_returns_results_per_row() -> None:
    results = validate_bronze_records(
        [
            {"customer_id": "1", "phone": "3001234567", "source": "crm"},
            {"customer_id": "", "phone": "3001234567", "source": ""},
        ]
    )

    assert len(results) == 2
    assert results[0]["errors"] == []
    assert results[1]["errors"]


def test_run_data_quality_checks_summarizes_failures() -> None:
    summary = run_data_quality_checks(
        [
            {"customer_id": "1", "phone": "3001234567", "source": "crm"},
            {"customer_id": "", "phone": "3001234567", "source": ""},
        ]
    )

    assert summary["total_rows"] == 2
    assert summary["failed_rows"] == 1
    assert summary["passed_rows"] == 1


def test_run_bronze_quality_checks_uses_default_input() -> None:
    summary = run_bronze_quality_checks()

    assert summary["total_rows"] == 3
