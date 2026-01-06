import pandas as pd
import yfinance as yf
from pathlib import Path

def fetch_market_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    """
    Fetch historical price data.
    """
    data = yf.Ticker(ticker).history(start=start, end=end)
    if data.empty:
        return ValueError(f"No data retrieved for {ticker} from {start} to {end}")
    required_cols = {"Open", "High", "Low", "Close", "Volume"}
    missing = required_cols - set(data.columns)
    if missing:
        return ValueError("Missing Columns:", missing)
    data["Close"] = data["Adj Close"] if "Adj Close" in data else data["Close"]
    
    data = data.dropna().drop_duplicates().sort_index()
    data.index = pd.to_datetime(data.index)
    
    raw_dir = Path(__file__).resolve().parents[1] / "data" / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    file_path = raw_dir / f"{ticker}_{start}_{end}.csv"
    data.to_csv(file_path)

    print(f"Successfully retrieved data for {ticker} from {start} to {end}")
    return data