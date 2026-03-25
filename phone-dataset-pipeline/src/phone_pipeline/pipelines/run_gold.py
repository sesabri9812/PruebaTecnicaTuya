from phone_pipeline.processing.gold import run_gold_pipeline


if __name__ == "__main__":
    result = run_gold_pipeline()

    print("=== GOLD TABLE ===")
    for row in result["table"][:5]:
        print(row)

    print("\n=== GOLD METRICS ===")
    print(result["metrics"])