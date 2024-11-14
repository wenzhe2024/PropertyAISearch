import sqlite3

# 连接到 SQLite 数据库，如果文件不存在则会创建一个新的数据库文件
conn = sqlite3.connect('../db/example.db')  # 创建或打开名为 'example.db' 的 SQLite 数据库
cursor = conn.cursor()



# 创建一个表
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT
    )
''')

# 插入数据
cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", ("Alice", 30, "alice@example.com"))
cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", ("Bob", 25, "bob@example.com"))

# 查询数据
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# 提交事务
conn.commit()

# 关闭连接
conn.close()
