def is_valid(step: str, result) -> bool:
    if result is None:
        return False
    if step == "fetch_market_data" and len(result) < 50:
        return False
    return True