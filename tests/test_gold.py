from __future__ import annotations

from phone_pipeline.curated.gold import build_gold_dataset, run_gold_pipeline


def test_build_gold_dataset_keeps_only_valid_contacts_in_valid_contacts() -> None:
    result = build_gold_dataset(
        [
            {"customer_id": "1", "source": "crm", "phone_e164": "+573001234567", "is_valid_phone": True},
            {"customer_id": "2", "source": "web", "phone_e164": None, "is_valid_phone": False},
        ]
    )

    assert result["total_records"] == 2
    assert result["valid_records"] == 1
    assert result["invalid_records"] == 1
    assert len(result["valid_contacts"]) == 1


def test_run_gold_pipeline_returns_summary_from_silver_data() -> None:
    result = run_gold_pipeline()

    assert result["total_records"] == 3
    assert result["valid_records"] == 2
