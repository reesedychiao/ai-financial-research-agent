from tools import data_fetcher, feature_engineer, analysis
from explainer import generate_explanation

def run_pipeline(ticker: str, start: str, end: str) -> dict:
    data = data_fetcher.fetch_market_data(ticker, start, end)
    features = feature_engineer.engineer_features(data)
    info = analysis.run_baseline_model(features)

    interpretation = interpret_metrics(info['metrics'])
    explanation = generate_explanation(
        info['metrics'],
        interpretation
    )

    return {
        **info,
        "interpretation": interpretation,
        "explanation": explanation
    }

def interpret_metrics(metrics: dict) -> str:
    lines = []

    if metrics["Average Daily Return"] > 0:
        lines.append("The asset shows positive average daily returns.")
    else:
        lines.append("The asset shows negative or flat average daily returns.")

    if metrics["Return Volatility (Std Dev)"] > 0.02:
        lines.append("Volatility is relatively high, indicating higher risk.")
    else:
        lines.append("Volatility is relatively low, indicating stable price movement.")

    if metrics["Trend R²"] < 0.1:
        lines.append("Returns do not show a strong directional trend.")

    return " ".join(lines)
