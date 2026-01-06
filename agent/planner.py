class PlannerAgent:
    def create_plan(self, user_query: str) -> list:
        """
        Convert a user query into a structured task plan.
        """
        plan = [
            "identify_companies",
            "fetch_market_data",
            "engineer_features",
            "run_analysis",
            "summarize_results"
        ]
        return plan