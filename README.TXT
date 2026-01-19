the agent flow from planning -> execution -> reflection, the tool is too naive rn for this stuctured approch.   

`schema.py` defines the pydantic models for the agent to follow an in bound response, 
`memory.py` defines the memory class for the agent to store the history of the conversation, 
`planner.py` defines the planner class for the agent to plan the steps to solve the problem, 
`executor.py` defines the executor class for the agent to execute the steps, 
`reflector.py` defines the reflector class for the agent to reflect on the steps and improve them, 
`llm.py` defines the llm class for the agent to call the llm, 
`tools.py` defines the tools for the agent to use, 
`log.py` defines the log class for the agent to log the steps, 
`agent.py` defines the agent class for the agent to run the steps. 

