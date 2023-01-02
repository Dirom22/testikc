from peewee import *

conn = SqliteDatabase('db2.sqlite')

class Students(Model):
	id = PrimaryKeyField(column_name = 'id') 
	name = CharField(column_name = 'name')
	surname = CharField(column_name = 'surname')
	age = IntegerField(column_name = 'age')
	city = CharField(column_name = 'city')

	class Meta:
		database = conn

class Courses(Model):
	id = PrimaryKeyField(column_name = 'id')
	name = CharField(column_name = 'name')
	time_start = DateTimeField(column_name = 'time_start')
	time_end = DateTimeField(column_name = 'time_end')

	class Meta:
		database = conn

class Student_courses(Model):
	student_id = ForeignKeyField(Students, to_field='id')
	courses_id = ForeignKeyField(Courses, to_field='id')

	class Meta:
		database = conn
		
st_30 = Students.select().where(Students.age > 30)
for i in st_30:
    print('студенты старше 30 лет: ',i.name)

st_py = Students.select().join(Student_courses).join(Courses).where(Student_courses.courses_id == 1)
for j in st_py:
    print('студенты изучающие python: ', j.name)

st_spb_py = Students.select().join(Student_courses).join(Courses).where(Student_courses.courses_id == 1, Students.city == 'Spb')
for k in st_spb_py:
    print('студенты изучающие python в СПб: ', k.name)
