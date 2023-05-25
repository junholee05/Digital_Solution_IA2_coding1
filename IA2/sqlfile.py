import sqlite3

connection = sqlite3.connect("database.db")

with open("assets/userschema.sql") as f:
    connection.executescript(f.read())
connection.close()


