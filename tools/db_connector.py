from sqlalchemy import create_engine
from config.config import Config

class DatabaseConnector:
    def __init__(self):
        self.engine = create_engine(Config.DATABASE_URL)

    def query(self, sql_query):
        with self.engine.connect() as connection:
            result = connection.execute(sql_query)
            return [row for row in result]
    