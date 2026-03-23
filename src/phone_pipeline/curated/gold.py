from __future__ import annotations

from collections import Counter
from typing import Any

from phone_pipeline.processing.silver import build_silver_dataset


def build_gold_dataset(records: list[dict[str, Any]]) -> dict[str, Any]:
    valid_records = [record for record in records if record.get("is_valid_phone")]
    source_distribution = Counter(record.get("source", "unknown") for record in valid_records)

    return {
        "total_records": len(records),
        "valid_records": len(valid_records),
        "invalid_records": len(records) - len(valid_records),
        "valid_contacts": valid_records,
        "source_distribution": dict(source_distribution),
    }


def run_gold_pipeline() -> dict[str, Any]:
    return build_gold_dataset(build_silver_dataset())
