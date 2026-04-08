import sqlite3

#function for connecting to database
def connect(database):
    connection_cursor = sqlite3.connect(database)
    return connection_cursor

def new_user(username, password):
    sqlite3.connection_cursor.execute(
        """
        INSERT INTO users(username, password)
        VALUES (?, ?);
        """,
        (username, password)
    )
    sqlite3.connection.commit()