from django.contrib import admin
from .models import *

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
	list_display = ["name", "email", "date_of_birth"]

	class Meta:
		model = Teacher

class StudentAdmin(admin.ModelAdmin):
	list_display = ["name", "email"]

	class Meta:
		model = Student

class GroupAdmin(admin.ModelAdmin):
	list_display = ["title"]

	class Meta:
		model = Group

class GroupMembersAdmin(admin.ModelAdmin):
	list_display = ["title"]

	class Meta:
		model = GroupMembers

class TaskAdmin(admin.ModelAdmin):
	list_display = ["title", "discipline"]

	class Meta:
		model = Task

class AnswerAdmin(admin.ModelAdmin):
	list_display = ["title", "task", "student", "date_of_finish"]

	class Meta:
		model = Answer

class DisciplineAdmin(admin.ModelAdmin):
	list_display = ["title", "teacher"]

	class Meta:
		model = Discipline

class MarkAdmin(admin.ModelAdmin):
	list_display = ["mark", "answer"]

	class Meta:
		model = Mark

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Mark, MarkAdmin)
admin.site.register(GroupMembers, GroupMembersAdmin)
