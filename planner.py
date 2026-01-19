from llm import call_llm 
from schema import Plan 
from log import log

PLANNER_PROMPT = """ 
you are a planner agent. 
break the user goal into minimal executable steps. 
steps must be concrete and ordered. 

response ONLY in valid JSON: 
{ 
"steps": ["step1", "step2", ...] 
}
""" 
# the panner does no execulation, it only decomposes
def plan(goal: str) -> Plan:  
    log("PLANNING GOAL", goal)
    messages = [ 
        {"role": "system", "content": PLANNER_PROMPT}, 
        {"role": "user", "content": goal} 
    ] 
    log("SENDING TO LLM", str(messages))
    raw = call_llm(messages) 
    log("RAW LLM OUTPUT", raw)
    return Plan.model_validate_json(raw) 
