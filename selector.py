
'''
Coś co zwraca połączenie w zależności jak wygląda zmienna db_type w .env,
można wtedy skrócić kod w , user.py, stress_test.py
'''

import os
from dotenv import load_dotenv
from db import DatabaseManager

load_dotenv()


class DatabaseSelector:

    def __init__(self):
        postgres_config_str = os.getenv('POSTGRES_CONFIG')
        self.postgres_config = eval(postgres_config_str)
        sqlite_config_str = os.getenv('SQLITE_CONFIG')
        self.sqlite_config = eval(sqlite_config_str)
        self.db_type = os.getenv('db_type')


    def database_type(self):
        if self.db_type == 'postgresql':
            db_conn = DatabaseManager(**self.postgres_config)
        else:
            db_conn = DatabaseManager(**self.sqlite_config)

        return db_conn