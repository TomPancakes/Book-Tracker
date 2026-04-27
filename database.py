#BOOK TRACKER APP W/ DATABASE INTEGRATION

#Import bulit in sqlite3 module
import sqlite3 

con = sqlite3.connect("books.db") #Create new SQLite Database to save locally

cur = con.cursor() #Database cursor allows to execute queries

cur.execute("CREATE TABLE IF NOT EXISTS books(title, status)")


def insert(entry, status):
    query = """
    INSERT INTO books (title, status)
    VALUES (:title, :status);

    """
    cur.execute(query, {"title": entry, "status": status})
    con.commit() #actually commit to database


def delete(name):
    query = """
    DELETE FROM books WHERE title = :title
    """
    cur.execute(query, {"title": name})
    con.commit() #actually commit to database

def modify_entry(id, title, score, status):
    pass

def get_entries():
    cur.execute("SELECT title, status FROM books")
    return cur.fetchall()


#If you want to access the database in terminal: 
# sqlite3 books.db
