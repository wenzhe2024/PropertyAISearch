from models.llm_wrapper import LLM
from models.text2sql import Text2SQL
from models.text2api import Text2API

def generate_response(tasks):
    llm = LLM()
    responses = []
    
    for task in tasks:
        if task["task_type"] == "Text2SQL":
            responses.append(Text2SQL().execute(task["query"]))
        elif task["task_type"] == "Text2API":
            responses.append(Text2API().execute(task["query"]))
    
    return llm.combine_responses(responses)
