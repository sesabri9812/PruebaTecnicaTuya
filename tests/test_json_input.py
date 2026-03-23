from __future__ import annotations

import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_JSON_PATH = PROJECT_ROOT / "data" / "bronze" / "phones_input.json"


def test_phones_input_json_is_valid_json() -> None:
    content = INPUT_JSON_PATH.read_text(encoding="utf-8")

    assert content.strip(), "phones_input.json should not be empty"

    parsed_data = json.loads(content)

    assert isinstance(parsed_data, list), "phones_input.json should contain a top-level JSON array"
