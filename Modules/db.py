import sqlite3

#function for connecting to database
def connect(database):
    conn = sqlite3.connect(database)
    
    return conn

def new_user(conn,username, password_hash):
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO users(username, password)
        VALUES (?, ?);
        """,
        (username, password_hash)
    )
    conn.commit()