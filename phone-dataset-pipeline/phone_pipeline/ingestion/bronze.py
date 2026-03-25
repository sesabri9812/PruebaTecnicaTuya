from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_INPUT_PATH = PROJECT_ROOT / "data" / "bronze" / "phones_input.json"


def load_bronze_data(input_path: str | Path = DEFAULT_INPUT_PATH) -> list[dict[str, Any]]:
    """Load raw phone data from the bronze JSON file."""
    json_path = Path(input_path)

    with json_path.open("r", encoding="utf-8") as file:
        raw_data = json.load(file)

    if not isinstance(raw_data, list):
        raise ValueError("Bronze input data must be a JSON array")

    return raw_data


if __name__ == "__main__":
    print(load_bronze_data())
