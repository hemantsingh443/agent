from llm import call_llm 
from schema import AgentStep 
from tools import search, calculate
from memory import AgentMemory 

SYSTEM_PROMPT = """
you are a reasoning agent. 
you must always respond in valid JSON matching this schema: 

{ 
"thought":string, 
"action":"search" | "calculate" | "final_answer",
"action_input":string | null  
} 

do NOT explain outside JSON.
"""  

class Agent: 
    def __init__(self): 
        self.memory = AgentMemory() 
    
    def run(self, user_input: str): 
        while True: 
            messages = [ 
                {"role": "system", "content": SYSTEM_PROMPT},  
                {"role": "user", "content": user_input}, 
                {"role": "assistant", "content": self.memory.dump()} 
            ] 
            raw = call_llm(messages) 
            step = AgentStep.model_validate_json(raw) 

            self.memory.add( 
                f"Thought: {step.thought}\n"
                f"action: {step.action}\n"
                f"Input: {step.action_input}\n"
            ) 
            if step.action == "search": 
                result = search(step.action_input) 
                self.memory.add(f"Observation: {result}") 
            
            elif step.action == "calculate": 
                result = calculate(step.action_input) 
                self.memory.add(f"Observation:{result}") 
            
            elif step.action == "final_answer": 
                return step.action_input 


agent = Agent()
answer = agent.run("What is 12 * (5 + 3)?")
print(answer)
