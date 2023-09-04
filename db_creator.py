import os
from dotenv import load_dotenv
from db_connection_pool import ConnectionPool

load_dotenv()


class DatabaseCreator:
    def __init__(self):
        postgres_config_str = os.getenv('POSTGRES_CONFIG')
        self.postgres_config = eval(postgres_config_str)
        sqlite_config_str = os.getenv('SQLITE_CONFIG')
        self.sqlite_config = eval(sqlite_config_str)
        self.db_type = os.getenv('db_type')


    def create_connection(self):
        if self.db_type == 'postgresql':
            try:
                conn = ConnectionPool(**self.postgres_config)
            except Exception as exp:
                print("Error:", exp)
        else:
            try:
                conn = ConnectionPool(**self.sqlite_config)
            except Exception as exp:
                print("Error:", exp)
        return conn
    

    def create_database(self):
        if self.db_type == 'postgresql':
            conn = self.create_connection().get_connection()
            conn.autocommit = True
            curr = conn.cursor()
            try:
                curr.execute('CREATE DATABASE db_cs_threading;')
            except Exception as exp:
                print("Error:", exp)


    def create_main_table(self):
        conn = self.create_connection().get_connection()
        curr = conn.cursor()
        query = """CREATE TABLE user_info (
                    user_id SERIAL PRIMARY KEY,
                    user_name VARCHAR(50) UNIQUE,
                    password VARCHAR(50),
                    is_admin BOOLEAN NOT NULL);"""
        try:
            curr.execute(query)
            conn.commit()
        except Exception as exp:
                print("Error:", exp)
        
if __name__ == '__main__':
    creator = DatabaseCreator()
    creator.create_database()
    creator.create_main_table()