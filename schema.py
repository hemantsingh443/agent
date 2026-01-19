from pydantic import BaseModel 
from typing import Literal, Optional 

class AgentStep(BaseModel): 
    thought: str 
    action: Literal["search", "calculate", "final_answer"]  
    action_input: Optional[str]  

  