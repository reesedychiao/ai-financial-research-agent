import pandas as pd

def engineer_features(price_df: pd.DataFrame, window: int=20) -> pd.DataFrame:
    df = price_df.copy()
    
    df['returns'] = df['Close'].pct_change()
    df['volatility'] = df['returns'].rolling(window).std()
    df['rolling_mean'] = df['returns'].rolling(window).mean()
    df['cumulative_return'] = (1 + df['returns']).cumprod() - 1

    df = df.dropna()
    assert not df.isnull().values.any(), "NaNs present in engineered features"

    print("Feature engineering complete!")
    print(
        df[['returns', 'volatility', 'cumulative_return']].describe().round(4)
    )
    return df