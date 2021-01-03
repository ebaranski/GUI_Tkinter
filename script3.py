import mysql.connector
from mysql.connector import errorcode


def insert(item, quantity, price):
    try:
        sStmt = "INSERT INTO store (item, quantity, price) VALUES(%s, %s, %s)"
        cursor.execute(sStmt, [item, quantity, price])
        conn.commit()
        # print("affected rows = {}".format(cursor.rowcount))
    except Exception as e:
        print(str(e))
        cursor.close()
        conn.close()
        exit()


# establishing the connection
try:
    conn = mysql.connector.connect(
        user="u744618245_eric",
        password="Uu744618245",
        host="185.201.11.86",
        database="u744618245_python")

    # Turn off autocommit (only way manual commit would work)
    # Could also set autocommit = TRUE and not use manual commit
    conn.autocommit = False

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

# Creating a cursor object
cursor = conn.cursor()

# Determine if table exist, if not create
sqlStmt = "SHOW TABLES LIKE 'store'"
cursor.execute(sqlStmt)
result = cursor.fetchone()
if not result:
    sqlStmt = '''CREATE TABLE store(
                item VARCHAR(50),
                quantity INTEGER,
                price REAL,
                PRIMARY KEY (item)
                )'''

    cursor.execute(sqlStmt)
    # according to mysql docs, 'create table' does auto-commit

    # insert initial data
    insert('Wine Glass', 8, 10.5)
    insert('Water Glass', 10, 5)
    insert('Coffee Cut', 20, 9.95)

cursor.close()
conn.close()
