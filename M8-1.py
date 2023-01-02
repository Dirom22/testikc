import sqlite3
from datetime import datetime

conn = sqlite3.connect('db2.sqlite')

cursor = conn.cursor()

#cursor.execute("""CREATE TABLE Students (id INTEGER PRIMARY KEY, name Varchar(25), surname Varchar(25), age int, city Varchar(25))""")
#cursor.execute("""CREATE TABLE Courses (id INTEGER PRIMARY KEY, name Varchar(20), time_start datetime, time_end datetime)""")

#courses = [(1, 'python', '21.07.21', '21.08.21'),
#			(2, 'java', '13.07.21', '16.08.21')]

#students = [(1, 'Max', 'Brooks', 24, 'Spb'),
#			(2, 'John', 'Stones', 15, 'Spb'),
#			(3, 'Andy', 'Wings', 45, 'Manhester'),
#			(4, 'Kate', 'Brooks', 34, 'Spb')]

#student_courses = [(1, 1), (2, 1), (3, 1), (4, 2)]

#cursor.execute("""CREATE TABLE Student_courses (
#												student_id INTEGER NOT NULL, 
#												course_id INTEGER NOT NULL, 
#												FOREIGN KEY (student_id) REFERENCES Students (id) 
#												FOREIGN KEY (course_id) REFERENCES Courses (id))""")

#cursor.executemany("INSERT INTO Students VALUES (?, ?, ?, ?, ?)", students)
#cursor.executemany("INSERT INTO Courses VALUES (?, ?, ?, ?)", courses)
#cursor.execute("INSERT INTO Student_courses (student_id, course_id) VALUES (?, ?)", (1, 1))
#cursor.execute("INSERT INTO Student_courses (student_id, course_id) VALUES (?, ?)", (2, 1))
#cursor.execute("INSERT INTO Student_courses (student_id, course_id) VALUES (?, ?)", (3, 1))
#cursor.execute("INSERT INTO Student_courses (student_id, course_id) VALUES (?, ?)", (4, 2))
#cursor.execute("DROP TABLE Students")
#conn.commit()

conn.close()