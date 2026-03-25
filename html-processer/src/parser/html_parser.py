from html.parser import HTMLParser


class HTMLImageParser(HTMLParser):

    def __init__(self, base_path: Path, encoder: ImageEncoder):
        super().__init__()
        self.base_path = base_path
        self.encoder = encoder
        self.result_html = []
        self.success = []
        self.fail = []

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            attrs_dict = dict(attrs)
            src = attrs_dict.get("src")

            if src:
                image_path = self.base_path / src
                encoded = self.encoder.encode(image_path)

                if encoded:
                    new_src = f"data:image;base64,{encoded}"
                    attrs_dict["src"] = new_src
                    self.success.append(src)
                else:
                    self.fail.append(src)

            attrs_str = " ".join(f'{k}="{v}"' for k, v in attrs_dict.items())
            self.result_html.append(f"<img {attrs_str}>")
        else:
            attrs_str = " ".join(f'{k}="{v}"' for k, v in attrs)
            self.result_html.append(f"<{tag} {attrs_str}>")

    def handle_endtag(self, tag):
        self.result_html.append(f"</{tag}>")

    def handle_data(self, data):
        self.result_html.append(data)

    def get_html(self):
        return "".join(self.result_html)