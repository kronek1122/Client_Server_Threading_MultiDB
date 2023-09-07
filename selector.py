import os
from dotenv import load_dotenv
from db import DatabaseManager
from db_connection_pool import ConnectionPool

load_dotenv()


class DatabaseSelector:

    def __init__(self):
        postgres_config_str = os.getenv('POSTGRES_CONFIG')
        self.postgres_config = eval(postgres_config_str)
        sqlite_config_str = os.getenv('SQLITE_CONFIG')
        self.sqlite_config = eval(sqlite_config_str)
        self.db_type = os.getenv('db_type')


    def connection_db_manager(self):
        if self.db_type == 'postgresql':
            db_conn = DatabaseManager(**self.postgres_config)
        else:
            db_conn = DatabaseManager(**self.sqlite_config)
        return db_conn
    

    def connection_conn_pool(self):
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


    def database_type(self):
        return self.db_type
