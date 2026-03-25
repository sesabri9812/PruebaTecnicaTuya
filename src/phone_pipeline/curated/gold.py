from __future__ import annotations

from collections import Counter
from datetime import datetime
from typing import Any

from phone_pipeline.processing.silver import build_silver_dataset

def build_gold_table(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Convierte registros silver en estructura tabular (filas)
    Lista para ser usada en motores tipo Iceberg / Athena / BI
    """
    gold_rows = []

    for record in records:
        if record.get("is_valid_phone"):
            gold_rows.append({
                "phone": record.get("phone"),
                "normalized_phone": record.get("normalized_phone"),
                "source": record.get("source", "unknown"),
                "ingestion_date": datetime.utcnow().isoformat(),
                "is_valid": True
            })

    return gold_rows



def build_gold_metrics(records: list[dict[str, Any]]) -> dict[str, Any]:
    """
    Genera KPIs de calidad y distribución
    """
    total_records = len(records)
    valid_records = [r for r in records if r.get("is_valid_phone")]
    invalid_records = total_records - len(valid_records)

    source_distribution = Counter(
        r.get("source", "unknown") for r in valid_records
    )

    quality_score = (len(valid_records) / total_records * 100) if total_records > 0 else 0

    return {
        "total_records": total_records,
        "valid_records": len(valid_records),
        "invalid_records": invalid_records,
        "quality_score": round(quality_score, 2),
        "source_distribution": dict(source_distribution),
        "generated_at": datetime.utcnow().isoformat()
    }


def run_gold_pipeline() -> dict[str, Any]:
    """
    Ejecuta todo el flujo GOLD:
    - Toma datos desde silver
    - Genera tabla (para Iceberg / BI)
    - Genera métricas (para dashboard)
    """
    silver_data = build_silver_dataset()

    gold_table = build_gold_table(silver_data)
    gold_metrics = build_gold_metrics(silver_data)

    return {
        "gold_table": gold_table,
        "gold_metrics": gold_metrics
    }