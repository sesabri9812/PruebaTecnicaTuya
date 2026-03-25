class HTMLProcessor:

    def __init__(self, paths):
        self.finder = HTMLFileFinder(paths)
        self.encoder = ImageEncoder()

    def process(self):
        files = self.finder.find_files()

        final_result = {
            "success": {},
            "fail": {}
        }

        for file_path in files:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            parser = HTMLImageParser(file_path.parent, self.encoder)
            parser.feed(content)

            new_file = file_path.with_name(file_path.stem + "_processed.html")

            with open(new_file, "w", encoding="utf-8") as f:
                f.write(parser.get_html())

            final_result["success"][str(file_path)] = parser.success
            final_result["fail"][str(file_path)] = parser.fail

        return final_result