from __future__ import annotations

from phone_pipeline.processing.silver import build_silver_dataset, transform_to_silver


def test_transform_to_silver_adds_phone_e164_and_validation_flags() -> None:
    records = [
        {"customer_id": "1", "phone": "300-123-4567", "source": "crm"},
        {"customer_id": "3", "phone": "invalid_phone", "source": "callcenter"},
    ]

    result = transform_to_silver(records)

    assert result[0]["phone_e164"] == "+573001234567"
    assert result[0]["is_valid_phone"] is True
    assert result[1]["phone_e164"] is None
    assert result[1]["is_valid_phone"] is False


def test_build_silver_dataset_reads_from_bronze_input() -> None:
    result = build_silver_dataset()

    assert len(result) == 3
    assert any(record["phone_e164"] == "+573001234567" for record in result)
