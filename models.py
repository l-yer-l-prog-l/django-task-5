from django.db import models

# Create your models here.
class Teacher(models.Model):
	name          = models.CharField('Имя',max_length=50)
	email         = models.EmailField('Электронная почта')
	date_of_birth = models.DateField('Дата рождения')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name        = 'Учитель'
		verbose_name_plural = 'Учителя'

class Group(models.Model):
	title      = models.CharField('Группа', max_length=50)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = 'Группы'

class Discipline(models.Model):
	title   = models.CharField('Урок', max_length=100)
	teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
	group   = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name        = 'Дисциплина'
		verbose_name_plural = 'Дисциплины'

class Student(models.Model):
	name          = models.CharField('Имя', max_length=50)
	email         = models.EmailField('Электронная почта')
	date_of_birth = models.DateField('Дата рождения')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name        = 'Студент'
		verbose_name_plural = 'Студенты'

class GroupMembers(models.Model):
	title   = models.CharField(max_length=50, null=True)
	group   = models.ForeignKey(Group, on_delete=models.CASCADE)
	student = models.ManyToManyField(Student)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name        = 'Участник группы'
		verbose_name_plural = 'Участники групп'


class Task(models.Model):
	title          = models.CharField('Задание', max_length=100)
	description    = models.TextField('Описание')
	date_of_start  = models.DateField('Дата начала')
	date_of_finish = models.DateField('Дата завершения', null=True)
	discipline     = models.ForeignKey(Discipline, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name        = 'Задание'
		verbose_name_plural = 'Задания'

class Answer(models.Model):
	title          = models.CharField('Заголовок', max_length=50)
	task           = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
	student        = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
	description    = models.TextField('Описание')
	date_of_finish = models.DateField('Дата завершения', auto_now = True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name        = 'Ответ'
		verbose_name_plural = 'Ответы'

class Mark(models.Model):
	mark   = models.IntegerField('Оценка')
	answer = models.OneToOneField(Answer, on_delete=models.CASCADE)

	def __int__(self):
		return self.mark


	class Meta:
		verbose_name        = 'Оценка'
		verbose_name_plural = 'Оценки'


