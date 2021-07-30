import sqlite3
import os
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_products(conn):
    """
    Query all rows in the products table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_table_names(conn):
    cur=conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    rows = cur.fetchall()
    
    for row in rows:
        print(row)

def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

def insert_into_table(conn,table_name):
    cur=conn.cursor()
    cur.execute(f'PRAGMA table_info({table_name});')
    rows = cur.fetchall()
    for row in rows:
        print(row)


def main():
    basedir = os.path.abspath(os.path.dirname(__file__))
    database = r'reverse-proxy-meli.db'

    # create a database connection
    conn = create_connection(database)
    # select_table_names(conn)
    select_all_products(conn)
    #select_table_names(conn)

if __name__ == '__main__':
    main()