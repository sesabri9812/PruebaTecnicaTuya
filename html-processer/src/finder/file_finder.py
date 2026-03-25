from pathlib import Path
from typing import List


class HTMLFileFinder:

    def __init__(self, paths: List[str]):
        self.paths = paths

    def find_files(self) -> List[Path]:
        html_files = []

        for path in self.paths:
            p = Path(path)

            if p.is_file() and p.suffix == ".html":
                html_files.append(p)

            elif p.is_dir():
                html_files.extend(p.rglob("*.html"))

        return html_files