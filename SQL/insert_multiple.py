import sqlite3

try:
    connection = sqlite3.connect("Narun_DB.db")
    cursor = connection.cursor()
    insert_data_query = """
        INSERT INTO student(name,email,course,cgpa) VALUES (?,?,?,?)
        """
    student_records = [
        ("Gulshan","gulu123@gmail.com","CIVIL",7.0),
        ("Kerweenson","turbine6000cc@gmail.com","CIVIL",6.0),
        ("JustinBabhi","justinbabhi6969@gmail.com","AIML",9.9),
        ("Reepak","angangmuu@gmail.com","CIVIL",5.5)
        ]
    cursor.executemany(insert_data_query, student_records)
    connection.commit()
    print("All Student Records Inserted Successfully")
except sqlite3.Error as error:
    print(error)
finally:
    cursor.close()
    connection.close()
