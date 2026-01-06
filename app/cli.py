import argparse
from main import run_pipeline
import pandas as pd

def main():
    parser = argparse.ArgumentParser(
        description="Run financial baseline analysis on a given ticker"
    )
    parser.add_argument(
        "--ticker", type=str, required=True, help="Ticker symbol, e.g., AAPL"
    )
    parser.add_argument(
        "--start", type=str, required=True, help="Start date in YYYY-MM-DD"
    )
    parser.add_argument(
        "--end", type=str, required=True, help="End date in YYYY-MM-DD"
    )
    parser.add_argument(
        "--save", type=str, default=None, help="Optional: file path to save summary as CSV"
    )

    args = parser.parse_args()

    result = run_pipeline(args.ticker, args.start, args.end)

    print("\n=== Metrics Summary ===")
    print(result["summary_df"])

    print("\n=== Interpretation ===")
    print(result["interpretation"])

    print("\n=== LLM Explanation ===")
    print(result["explanation"])

    if args.save:
        result["summary_df"].to_csv(args.save, index=True)
        print(f"\nSaved summary to {args.save}")

if __name__ == "__main__":
    main()