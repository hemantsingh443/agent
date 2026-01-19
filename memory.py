class AgentMemory: 
    def __init__(self): 
        self.steps = [] 

    def add(self, step:str): 
        self.steps.append(step) 

    def dump(self) -> str: 
        return "\n".join(self.steps) 