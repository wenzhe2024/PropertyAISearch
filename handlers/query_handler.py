from handlers.task_planner import plan_tasks
from handlers.response_generator import generate_response
from models.llm_wrapper import LLM

def handle_query(query):
    llm = LLM()
    standardized_query = llm.standardize_query(query)
    tasks = plan_tasks(standardized_query)
    response = generate_response(tasks)
    return response
