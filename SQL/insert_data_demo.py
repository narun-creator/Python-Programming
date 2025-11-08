import sqlite3

try:
    connection = sqlite3.connect("Narun_db.db")
    cursor = connection.cursor()
    create_table_query = """
        INSERT INTO student(name,email,course,cgpa) VALUES (?,?,?,?)
        """
    student_data = ("Suraj","toijamsuraj@gmail.com","CIVIL",6.0)
    cursor.execute(create_table_query, student_data)
    connection.commit()
    print("Student Data Inserted successfully")
except sqlite3.Error as error:
    print(error)
finally:
    cursor.close()
    connection.close()
