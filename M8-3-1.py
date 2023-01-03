from peewee import *
from datetime import datetime

conn = SqliteDatabase('sq1.sqlite')

class Students(Model):
	id = PrimaryKeyField(column_name = 'id')
	name = CharField(column_name = 'name')
	surname = CharField(column_name = 'surname')
	age = IntegerField(column_name = 'age')
	sity = CharField(column_name = 'sity')

	class Meta:
		database = conn

class Courses(Model):
	id = PrimaryKeyField(column_name = 'id')
	name = CharField(column_name = 'name')
	time_start = DateTimeField(column_name = 'time_start')
	time_end = DateTimeField(column_name = 'time_end')

	class Meta:
		database = conn

class Students_Courses(Model):
	student_id = ForeignKeyField(Students, to_field = 'id')
	courses_id = ForeignKeyField(Courses, to_field = 'id')

	class Meta:
		database = conn

#Students.create_table()
#Courses.create_table()
#Students_Courses.create_table()

courses = [{'id':1, 'name':'python', 'time_start':'21.07.21', 'time_end':'21.08.21'}, 
			{'id':2, 'name':'java', 'time_start':'13.07.21', 'time_end':'16.08.21'}]

students = [{'id':1, 'name':'Max', 'surname':'Brooks', 'age':24, 'sity':'Spb'},
			{'id':2, 'name':'John', 'surname':'Stones', 'age':15, 'sity':'Spb'},
			{'id':3, 'name':'Andy', 'surname':'Wings', 'age':45, 'sity':'Manhester'},
			{'id':4, 'name':'Kate', 'surname':'Brooks', 'age':34, 'sity':'Spb'}]

student_courses = [{'student_id':1, 'courses_id':1}, 
					{'student_id':2, 'courses_id':1}, 
					{'student_id':3, 'courses_id':1}, 
					{'student_id':4, 'courses_id':2}]

#Students.insert_many(students).execute()
#Courses.insert_many(courses).execute()
#Students_Courses.insert_many(student_courses).execute()

for students in Students.select().where(Students.age > 30):
	print('Студенты старше 30 лет: ', students.name)

st_py = Students.select().join(Students_Courses).join(Courses).where(Courses.id == 1)
for i in st_py:
	print('Студенты изучающие Python: ', i.name)

st_py_spb = Students.select().join(Students_Courses).join(Courses).where(Students_Courses.courses_id == 1, Students.sity == 'Spb')
for x in st_py_spb:
	print('Студенты изучающие Python и живущие в СПб: ', x.name)

#cursor = conn.cursor()
#xc = cursor.execute("""SELECT name FROM sqlite_master 
#					WHERE type = 'table'""")
#print(xc.fetchall())
