from __future__ import annotations

from typing import Any


REQUIRED_FIELDS = ("customer_id", "phone", "source")


def validate_required_fields(record: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    for field in REQUIRED_FIELDS:
        value = record.get(field)
        if value is None or str(value).strip() == "":
            errors.append(f"Missing required field: {field}")

    return errors


def validate_bronze_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    validation_results: list[dict[str, Any]] = []

    for index, record in enumerate(records):
        validation_results.append(
            {
                "row_number": index,
                "customer_id": str(record.get("customer_id", "")),
                "errors": validate_required_fields(record),
            }
        )

    return validation_results
