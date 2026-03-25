from src.processor.html_processor import HTMLProcessor

def main():
    paths = [
        "data/input",
        "data/input/test.html"
    ]

    processor = HTMLProcessor(paths)
    result = processor.process()

    print(result)


if __name__ == "__main__":
    main()