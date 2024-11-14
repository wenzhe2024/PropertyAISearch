from handlers.query_handler import handle_query
from config.config import Config

from handlers.query_handler import handle_query

def main():
    print("欢迎使用房产中介服务！")
    while True:
        user_input = input("用户: ")
        if user_input.lower() in ["退出", "再见"]:
            print("中介: 感谢您的咨询，期待再次为您服务！")
            break
        response = handle_query(user_input)
        print("中介:", response)


if __name__ == "__main__":
    main()
