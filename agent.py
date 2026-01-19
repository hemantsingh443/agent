from planner import plan
from executor import execute_step
from reflector import reflect
from memory import AgentMemory

class Agent:
    def run(self, goal: str):
        memory = AgentMemory()

        plan_obj = plan(goal)
        memory.add(f"Plan: {plan_obj.steps}")

        final_answer = None

        for step in plan_obj.steps:
            memory.add(f"Executing step: {step}")
            final_answer = execute_step(step, memory)

        critique = reflect(goal, final_answer)

        if not critique.is_correct:
            memory.add(f"Reflection failed: {critique.reason}")
            return "Agent failed and needs retry."

        return final_answer

agent = Agent()
answer = agent.run("What is 12 * (5 + 3)?")
print(answer)
