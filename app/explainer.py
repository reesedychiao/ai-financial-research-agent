from openai import OpenAI
import os
from dotenv import load_dotenv

def generate_explanation(metrics: dict, interpretation: str) -> str:
    prompt = f"""
        You are a financial analyst.

        Metrics:
        {metrics}

        Interpretation:
        {interpretation}

        Explain this analysis clearly to a non-technical stakeholder.
    """

    load_dotenv()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": "You are a clear and concise financial analyst."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()