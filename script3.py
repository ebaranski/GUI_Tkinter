import mysql.connector
from mysql.connector import errorcode
import os


def connect_db():
    # establishing the connection
    try:
        conn = mysql.connector.connect(
            user=db_user,
            password=db_pass,
            host="185.201.11.86",
            database="u744618245_python")

        # Turn off autocommit (only way manual commit would work)
        # Could also set autocommit = TRUE and not use manual commit
        conn.autocommit = False
        return conn

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


def create_table(add_data=False):
    # Determine if table exist, if not create
    sql_stmt = "SHOW TABLES LIKE 'store'"
    cursor.execute(sql_stmt)
    result = cursor.fetchone()
    if not result:
        sql_stmt = '''CREATE TABLE store(
                    item VARCHAR(50),
                    quantity INTEGER,
                    price REAL,
                    PRIMARY KEY (item)
                    )'''

        # according to mysql docs, 'create table' does auto-commit
        cursor.execute(sql_stmt)

        # insert_db initial test data if requested
        if add_data:
            insert_db('Wine Glass', 8, 10.5)
            insert_db('Water Glass', 10, 5)
            insert_db('Coffee Cut', 20, 9.95)


def insert_db(item, quantity, price):
    try:
        db.reconnect()
        sql_stmt = "INSERT INTO store (item, quantity, price) VALUES(%s, %s, %s)"
        cursor.execute(sql_stmt, [item, quantity, price])
        db.commit()
        # print("affected rows = {}".format(cursor.rowcount))
    except Exception as e:
        print(str(e))
        cursor.close()
        db.close()
        exit()


def select_db():
    db.reconnect()
    sql_stmt = "SELECT * FROM store"
    cursor.execute(sql_stmt)
    rows = cursor.fetchall()
    return rows


def delete_db(item):
    db.reconnect()
    sql_stmt = "DELETE FROM store WHERE item = %s"
    cursor.execute(sql_stmt, [item])
    db.commit()


def update_db(item, quantity, price):
    db.reconnect()
    sql_stmt = "UPDATE store SET quantity=%s, price=%s WHERE item = %s"
    cursor.execute(sql_stmt, [quantity, price, item])
    db.commit()


# Store credentials as Environment Variables (not as plain text)
# Control Panel >> System >> About >> Advance System Settings >> Environment Variables
db_user = os.environ.get('HOSTINGER_PYTHON_DB_USER')
db_pass = os.environ.get('HOSTINGER_PYTHON_DB_PASSWORD')

# get connection to database
db = connect_db()

# Creating a cursor object (return data as dictionary)
cursor = db.cursor(dictionary=True)

# Create table and test data if needed
create_table(add_data=True)

delete_db('Wine Glass')

update_db('Water Glass', 25, 6.99)

# get data and print
for row in select_db():
    print(f"{row.get('item')}     {row.get('quantity')}     {row.get('price')}")

cursor.close()
db.close()
