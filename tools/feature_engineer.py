def engineer_features(price_df):
    price_df['returns'] = price_df['close'].pct_change()
    price_df['volatility'] = price_df['returns'].rolling(20).std()
    return price_df.dropna()