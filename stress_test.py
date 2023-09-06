import os
import threading
from selector import DatabaseSelector



def stress_test():
    users = db.get_users()
    return users

if __name__ == "__main__":

    db = DatabaseSelector().database_type()
    NUM_CONNECTIONS = 10000  # Number of concurrent connections

    threads = []
    for _ in range(NUM_CONNECTIONS):
        thread = threading.Thread(target=stress_test)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()