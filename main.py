from handlers.query_handler import handle_query
from config.config import Config

from handlers.query_handler import handle_query

def main():

    """
        while True:
        user_input = input("用户: ")
        if user_input.lower() in ["退出", "再见"]:
            print("中介: 感谢您的咨询，期待再次为您服务！")
            break
        response = handle_query(user_input)
        print("中介:", response)

    """
    # 文件名
    file_name = "test/questions.txt"

    # 打开文件并逐行读取
    with open(file_name, "r", encoding="utf-8") as file:
        queries = file.readlines()

    # 去掉每行的换行符并打印
    queries = [query.strip() for query in queries]
    print ("*********************************")
    for query in queries:
        response = handle_query(query)

if __name__ == "__main__":
    main()
