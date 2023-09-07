from selector import DatabaseSelector


class DatabaseCreator:

    def __init__(self):
        self.db_type = DatabaseSelector().database_type()


    def create_connection(self):
        conn = DatabaseSelector().connection_conn_pool()
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