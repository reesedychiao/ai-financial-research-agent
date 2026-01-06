from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

def run_baseline_model(price_df: pd.DataFrame, price_col: str = "Close") -> dict:
    df = price_df.copy()
    
    if price_col not in df.columns:
        return ValueError(f"'{price_col}' is not a column in the input data")

    X = np.arange(len(df['returns'])).reshape(-1, 1)
    y = df['returns'].values

    model = LinearRegression()
    model.fit(X, y)
    trend_slope = model.coef_[0]
    r_squared = model.score(X, y)

    metrics = {
        "Average Daily Return": df['returns'].mean(),
        "Return Volatility (Std Dev)": df['returns'].std(),
        "Cumulative Return": (1 + df['returns']).prod() - 1,
        "Trend Slope (Returns vs Time)": trend_slope,
        "Trend R²": r_squared,
    }

    summary_df = pd.DataFrame.from_dict(
        metrics, orient="index", columns=["Value"]
    )

    return {
        "metrics": metrics,
        "summary": summary_df,
        "model": model,
    }