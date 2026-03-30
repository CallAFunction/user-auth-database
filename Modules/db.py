import sqlite3

def connect(database):
    connection = sqlite3.connect('../accounts.db')