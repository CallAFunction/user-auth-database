import sqlite3

#function for connecting to database
def connect(database):
    connection_cursor = sqlite3.connect(database)
    return connection_cursor

def new_user(username, password):
    connection_cursor.execute(
        f"""
        INSERT INTO users (username, password)
        values({username}, {password})
        """
    )