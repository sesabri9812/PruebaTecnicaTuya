import base64
from pathlib import Path
from typing import Optional


class ImageEncoder:

    @staticmethod
    def encode(image_path: Path) -> Optional[str]:
        try:
            with open(image_path, "rb") as img:
                encoded = base64.b64encode(img.read()).decode("utf-8")
            return encoded
        except Exception:
            return None