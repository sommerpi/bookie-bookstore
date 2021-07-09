import sqlite3
import os

db_path =  os.path.abspath("books.db")


def connect():
  conn=sqlite3.connect(db_path)
  cur=conn.cursor()
  cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
  conn.commit()
  conn.close()


def insert(title, author, year, isbn):
  conn = sqlite3.connect(db_path)
  cur=conn.cursor()
  cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year,isbn))
  conn.commit()
  conn.close()


def view():
  conn = sqlite3.connect(db_path)
  cur=conn.cursor()
  cur.execute("SELECT * FROM book")
  rows = cur.fetchall()
  conn.close()
  return rows

def delete(id):
  conn = sqlite3.connect(db_path)
  cur=conn.cursor()
  cur.execute("DELETE FROM book WHERE id=?", (id,))
  conn.commit()
  conn.close()

def update(id, title, author, year, isbn):
  conn = sqlite3.connect(db_path)
  cur=conn.cursor()
  cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year,isbn, id))
  conn.commit()
  conn.close()

def search(title="", author="", year="", isbn=""):
  conn = sqlite3.connect(db_path)
  cur=conn.cursor()
  cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
  rows = cur.fetchall()
  conn.close()
  return rows

def main():
  connect()
  #insert("The Well of Loneliness", "Jonathan Cape", 1928, 9780385416092)
  #delete(3)
  #update(6, "The well of loneliness", "Radclyffe Hall", 1967, 999999)
  #print(view())
  print(search(author="Radclyffe Hall"))

if __name__ == "__main__":
  main()