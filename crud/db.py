import sqlite3

def db_connection():
    con = sqlite3.connect("users.db")
    cursor = con.cursor()

    return con, cursor
