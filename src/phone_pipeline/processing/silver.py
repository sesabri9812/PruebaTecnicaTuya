from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from phone_pipeline.data_quality.quality_runner import run_data_quality_checks
from phone_pipeline.ingestion.bronze import load_bronze_data
from phone_pipeline.utils.phone_utils import normalize_phone_to_e164


PROJECT_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_OUTPUT_PATH = PROJECT_ROOT / "data" / "silver" / "phones_cleaned.json"


def transform_to_silver(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    cleaned: list[dict[str, Any]] = []

    for record in records:
        phone_raw = str(record.get("phone", ""))
        phone_e164 = normalize_phone_to_e164(phone_raw)
        cleaned.append(
            {
                "customer_id": str(record.get("customer_id", "")),
                "phone_raw": phone_raw,
                "phone_e164": phone_e164,
                "is_valid_phone": phone_e164 is not None,
                "source": str(record.get("source", "")),
            }
        )

    return cleaned


def build_silver_dataset() -> list[dict[str, Any]]:
    bronze_records = load_bronze_data()
    return transform_to_silver(bronze_records)


def clean_data(output_path: str | Path = DEFAULT_OUTPUT_PATH) -> list[dict[str, Any]]:
    cleaned = build_silver_dataset()
    run_data_quality_checks(load_bronze_data())

    destination = Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(cleaned, indent=2), encoding="utf-8")

    return cleaned
