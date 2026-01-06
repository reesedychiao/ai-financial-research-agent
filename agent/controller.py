class AgentController:
    def __init__(self, planner, tools, evaluator):
        self.planner = planner
        self.tools = tools
        self.evaluator = evaluator
        self.state = {}

    def run(self, user_query: str):
        plan = self.planner.create_plan(user_query)

        for step in plan:
            result = self.execute_step(step)
            self.state[step] = result

            if not self.evaluator.is_valid(step, result):
                return self.handle_failure(step)

        return self.state


    def execute_step(self, step: str):
        return self.tools[step]()