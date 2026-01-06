def fetch_market_data(ticker: str, start, end):
    """
    Fetch historical price data.
    """
    data = api_call(ticker, start, end)
    return data