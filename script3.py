import mysql.connector
from mysql.connector import errorcode
import os

db = mysql.connector.connect()


def connect_db():
    # Store credentials as Environment Variables (not as plain text)
    # Control Panel >> System >> About >> Advance System Settings >> Environment Variables
    db_user = os.environ.get('HOSTINGER_PYTHON_DB_USER')
    db_pass = os.environ.get('HOSTINGER_PYTHON_DB_PASSWORD')

    # establishing the connection
    try:
        db = mysql.connector.connect(
            user=db_user,
            password=db_pass,
            host="185.201.11.86",
            database="u744618245_python")

        # Turn off autocommit (only way manual commit would work)
        # Could also set autocommit = TRUE and not use manual commit
        db.autocommit = False

        # Creating a cursor object (return data as dictionary)
        cursor = db.cursor(dictionary=True)

        # create table if not found
        create_table()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
            exit()
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            exit()
        else:
            print(err)
            exit()


def create_table():
    sql_stmt = '''CREATE TABLE IF NOT EXISTS book(
                id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
                title VARCHAR(50),
                author VARCHAR(50),
                publish_year SMALLINT,
                isbn INTEGER
                )'''


    try:
        # define cursor
        cursor = db.cursor(dictionary=True)

        # according to mysql docs, 'create table' does auto-commit
        cursor.execute(sql_stmt)
    except mysql.connector.Error as err:
        print(err)
        exit()


def insert_db(title, author, year, isbn):
    try:
        db.reconnect()
        cursor = db.cursor(dictionary=True)

        sql_stmt = "INSERT INTO book (id, title, author, year, isbn) VALUES(%s, %s, %s, %s, %s)"
        cursor.execute(sql_stmt, [0, title, author, year, isbn])
        db.commit()
        # print("affected rows = {}".format(cursor.rowcount))
    except Exception as e:
        print(str(e))
        cursor.close()
        db.close()
        exit()


def select_db():
    db.reconnect()
    cursor = db.cursor(dictionary=True)

    sql_stmt = "SELECT * FROM store"
    cursor.execute(sql_stmt)
    rows = cursor.fetchall()
    return rows


def delete_db(item):
    db.reconnect()
    cursor = db.cursor(dictionary=True)

    sql_stmt = "DELETE FROM store WHERE item = %s"
    cursor.execute(sql_stmt, [item])
    db.commit()


def update_db(item, quantity, price):
    db.reconnect()
    cursor = db.cursor(dictionary=True)

    sql_stmt = "UPDATE store SET quantity=%s, price=%s WHERE item = %s"
    cursor.execute(sql_stmt, [quantity, price, item])
    db.commit()


def close_db():
    db.close()
