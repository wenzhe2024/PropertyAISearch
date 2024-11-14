def plan_tasks(query):
    # 模拟任务规划逻辑，根据标准化查询生成任务列表
    tasks = [
        {"task_type": "Text2SQL", "query": query},
        {"task_type": "Text2API", "query": query}
    ]
    return tasks
