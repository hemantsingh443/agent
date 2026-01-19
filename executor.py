from llm import call_llm 
from schema import ExecStep 
from tools import search, calculate  
from memory import AgentMemory 
from log import log

EXECUTOR_PROMPT = """ 
you are an executor agent. 
execute the current step and memory, decide the next action. 

response ONLY in valid JSON: 
{ 
"thought":"....", 
"action":"search" | "calculate" | "final_answer",
"action_input":string | null  
}
""" 
def execute_step(step: str, memory: AgentMemory) -> str: 
    while True:  
        log("CURRENT MEMORY", memory.dump() or "(empty)")
        log("EXECUTING STEP", step)
        messages = [ 
            {"role": "system", "content": EXECUTOR_PROMPT}, 
            {"role": "user", "content": f"step: {step}"}, 
            {"role": "assistant", "content": memory.dump()} 
        ] 

        log("SENDING TO LLM", str(messages))

        raw = call_llm(messages)   
        log("RAW LLM OUTPUT", raw)

        decision = ExecStep.model_validate_json(raw)  

        log(
            "PARSED DECISION",
            f"Thought: {decision.thought}\n"
            f"Action: {decision.action}\n"
            f"Input: {decision.action_input}"
        )
        memory.add(f"Thought: {decision.thought}") 

        
        if decision.action == "search": 
            log("TOOL CALL", f"search({decision.action_input})")
            obs = search(decision.action_input)
            memory.add(f"Observation: {obs}") 
            log("OBSERVATION", obs)

        elif decision.action == "calculate":
            log("TOOL CALL", f"calculate({decision.action_input})")
            obs = calculate(decision.action_input)
            memory.add(f"Observation: {obs}")
            log("OBSERVATION", obs)

        elif decision.action == "final_answer": 
            memory.add(f"Result: {decision.action_input}") 
            log("FINAL ANSWER", decision.action_input)
            return decision.action_input
     