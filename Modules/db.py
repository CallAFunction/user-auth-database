import sqlite3

#function for connecting to database
def connect(database):
    conn = sqlite3.connect(database)
    
    return conn

#function for creating new user 
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

def find_user_password(conn, username):
    cursor = conn.cursor()
    password = cursor.execute(
        """
        SELECT password FROM users
        WHERE username = ?;
        """,
        (username,)
    )
    result  = cursor.fetchone()
    if result is None:
        return None
    return result[0]
    