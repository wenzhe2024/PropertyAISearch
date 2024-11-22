from handlers.task_planner import plan_tasks
#from handlers.response_generator import generate_response
from models.llm_wrapper import LLM
from utils.intention_detector import detect_intention
from models.text2sql import text_to_sql
from tools.db_connector import DatabaseConnector

def handle_query(query):
    print("query: ", query)
    llm = LLM()
    standardized_query = standarize_query(query)
    # tasks = plan_tasks(standardized_query)
    related_tables = detect_intention(standardized_query)
    sql_query = text_to_sql(standardized_query, related_tables)
    print ("生成的SQL为： ", sql_query)


    dbconn = DatabaseConnector()
    response = dbconn.query(sql_query)
    # response = generate_response(tasks)
    print ("response: ", response)
    return response


def standarize_query(query):
    """
    对于用户的query进行标准化
    比如用户query中包含"好学校"，对于好学校需要定义，如果用decile来定义好学校
    那就需要把query提前转换成数据库更容易理解的文字。
    参数：
    - query(str): 用户的问题

    返回：
    - str: 修改之后的query。
    """
    # TODO:

    return query
