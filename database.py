#BOOK TRACKER APP W/ DATABASE INTEGRATION

#Import bulit in sqlite3 module
import sqlite3 

con = sqlite3.connect("books.db") #Create new SQLite Database to save locally

cur = con.cursor() #Database cursor allows to execute queries

cur.execute("CREATE TABLE IF NOT EXISTS books(id, title, rating, status)")



def insert_entry(entry, score, status):
    pass

def delete_entry(id):
    pass

def modify_entry(id, title, score, status):
    pass

def get_entries():
    pass


con.close()
