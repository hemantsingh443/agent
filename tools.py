def search(query:str)-> str: 
    return f"You searched for: {query}" 

def calculate(expr:str)-> str:  
    try: 
        return str(eval(expr)) 
    except Exception as e: 
        return f"Error: {str(e)}"