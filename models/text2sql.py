import openai
from utils.intention_detector import detect_intention
from utils.load_schema import extract_table_definition
from models.llm_wrapper import LLM
from sqlalchemy import text
import re


def filter_schema(related_tables):
    """
    根据给定的表名，抽取相关表的描述和字段描述。

    参数：
    - related_tables(list)：list of 表明

    返回：
    - str: 表的描述和字段描述，作为大模型调用的上下文。
    """
    schema_content = extract_table_definition()
    extracted_info = []

    for table in related_tables:
        if table in schema_content:
            table_info = schema_content[table]
            # 格式化输出，每个表的内容开头带 "## 表" 以保持结构一致
            extracted_info.append(f"{table_info.strip()}")

    return "\n\n".join(extracted_info)


def text_to_sql(question, related_tables):
    schema_definition = filter_schema(related_tables)
    #print (schema_definition)
    prompt = f"""
    你是一个智能的房产领域SQLite助手。 把用户的问题转换为SQLite语句。 下面是房产数据库的表结构定义：
    
    {schema_definition}
    
    根据上述表结构，请为以下问题生成一个 SQLite 查询：

    问题：{question}

    SQLite 查询：
    """
    #print ("prompt is: ", prompt)

    llm = LLM()

    try:
        response = llm.query(prompt)
        response = response.replace("sql\n", "", 1).strip()
        response = response.strip('```')

        #print ("获取到的sql为：\n", response)
        #sql_query = response.strip()
        return text(response)

    except openai.error.OpenAIError as e:
        print(f"意图检测失败: {e}")
        return []  # 如果出错，返回空列表