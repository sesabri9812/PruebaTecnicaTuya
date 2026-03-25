from __future__ import annotations

from phone_pipeline.ingestion.bronze import DEFAULT_INPUT_PATH, load_bronze_data


def test_load_bronze_data_reads_default_bronze_file() -> None:
    data = load_bronze_data()

    assert DEFAULT_INPUT_PATH.name == "phones_input.json"
    assert isinstance(data, list)
    assert len(data) == 3
