from pydantic import BaseModel 
from typing import Literal, Optional, List 

class Plan(BaseModel): 
    steps: List[str]

class ExecStep(BaseModel): 
    thought: str 
    action: Literal["search", "calculate", "final_answer"]  
    action_input: Optional[str]  

class Reflection(BaseModel): 
    is_correct: bool 
    reason: str
 


  