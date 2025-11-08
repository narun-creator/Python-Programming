import sqlite3
try:
    connection = sqlite3.connect("Narun_DB.db")
    cursor = connection.cursor()
    filter_query = "SELECT name, email, course, cgpa FROM student where course = ?"
    filter_value = ("CIVIL",)
    cursor.execute(filter_query, filter_value)
    result = cursor.fetchall()
    for row in result:
        print(row)
except sqlite3.Error as error:
    print(error)
finally:
    cursor.close()
    connection.close()
