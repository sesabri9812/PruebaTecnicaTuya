from __future__ import annotations

from collections import Counter
from typing import Any

from phone_pipeline.processing.silver import build_silver_dataset


def build_gold_table(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Dataset limpio para consumo en BI (tabla)
    """
    return [
        {
            "phone": record.get("phone"),
            "source": record.get("source"),
            "country_code": record.get("country_code"),
        }
        for record in records
        if record.get("is_valid_phone")
    ]


def build_gold_metrics(records: list[dict[str, Any]]) -> dict[str, Any]:
    """
    Métricas agregadas (KPI)
    """
    valid_records = [r for r in records if r.get("is_valid_phone")]

    source_distribution = Counter(
        r.get("source", "unknown") for r in valid_records
    )

    return {
        "total_records": len(records),
        "valid_records": len(valid_records),
        "invalid_records": len(records) - len(valid_records),
        "source_distribution": dict(source_distribution),
    }


def run_gold_pipeline() -> dict[str, Any]:
    """
    Orquesta la capa GOLD
    """
    silver_data = build_silver_dataset()

    return {
        "table": build_gold_table(silver_data),
        "metrics": build_gold_metrics(silver_data),
    }