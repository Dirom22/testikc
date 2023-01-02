import sqlite3
from datetime import datetime

conn = sqlite3.connect('db2.sqlite')

cursor = conn.cursor()

st_30 = cursor.execute("""SELECT name, age FROM Students WHERE age > 30""").fetchall()
st_py = cursor.execute("""SELECT Courses.name, Students.name
				FROM Student_courses, Courses, Students
				WHERE course_id = 1 = Courses.id  and student_id = Students.id""").fetchall()
st_spb_py = cursor.execute("""SELECT Students.name, Courses.name, Students.city  
                                FROM Students, Courses, Student_courses 
                                WHERE course_id = 1 = Courses.id and student_id = Students.id and Students.city = 'Spb'""").fetchall()

conn.close()

print(st_30)
print(st_py)
print(st_spb_py)