from django.db import models
from django.contrib.auth.models import User

yearChoices = (('All Years', 'All Years'),('I','I'),('II','II'),('III','III'),('IV','IV'))
sectionChoices =  (('A','A'),('B','B'),('C','C'),('D','D'))
branches = (('GLOBAL', 'GLOBAL'),('CSE', 'CSE'), ('MECH', 'MECH'), ('EEE', 'EEE'), ('ECE','ECE'), ('IT', 'IT'), ('CIVIL', 'CIVIL'), ('ECM', 'ECM'))

class Teacher(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	email = models.EmailField(max_length = 100)
	name = models.CharField(max_length = 25)
	bio = models.CharField(max_length = 200)
	subject = models.CharField(max_length = 25)

	def __str__(self):
		return self.name

class Post(models.Model):
	subject = models.CharField(max_length = 100)
	topic = models.CharField(max_length = 100, blank = True)
	description = models.TextField(max_length = 250)
	author = models.CharField(max_length = 25)
	links = models.CharField(max_length = 500, blank = True)
	branch = models.CharField(max_length = 20, choices = branches, default = 'GLOBAL')
	year = models.CharField(max_length = 20, choices = yearChoices, default = 'All Years')
	sections = models.CharField(max_length = 20, choices = sectionChoices, default = 'All Years')
	date_posted = models.DateTimeField(auto_now=True)
	time_posted = models.TimeField(auto_now=True)

	def __str__(self):
		return self.subject

class Student(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	email = models.EmailField(max_length = 100)
	name = models.CharField(max_length = 50)
	bio = models.CharField(max_length = 200)
	branch = models.CharField(max_length = 20, choices = branches, default = 'CSE')
	year = models.CharField(max_length = 20, choices = yearChoices, default = 'I')
	section = models.CharField(max_length = 20, choices = sectionChoices, default = 'A')


	def __str__(self):
		return self.name

