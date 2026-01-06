def generate_explanation(metrics, insights):
    prompt = f"""
    Explain the following financial analysis to a non-technical stakeholder:
    Metrics: {metrics}
    Insights: {insights}
    Limitations: data coverage, model simplicity
    """
    return call_llm(prompt)