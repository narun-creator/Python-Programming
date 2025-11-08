import sqlite3

try:
    #connect to the database
    connection = sqlite3.connect("SQL/Narun_DB.db")
    cursor = connection.cursor()
    #select and print data
    cursor.execute("SELECT * FROM student")
    print("Students in the database:")
    for row in cursor.fetchall():
        print(row)

except sqlite3.Error as e:
    print(f"sqLite Error: {e}")
finally:
    if connection:
        connection.close()
