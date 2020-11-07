from django.shortcuts import render, get_object_or_404, redirect
from .models import Teacher, Student, Task, Discipline
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, AnswerForm

def index(request):
	return render(request, 'main/index.html')

def teacher(request):
	teachers_list = Teacher.objects.all()
	return render(request, 'main/teacher.html', {'teachers_list': teachers_list})

def teacher_open(request, pk):
	teacher = get_object_or_404(Teacher, pk=pk)
	return render(request, 'main/teacher_open.html', {'teacher': teacher})

def student(request):
	students_list = Student.objects.all()
	return render(request, 'main/student.html', {'students_list': students_list})

def students_open(request, pk):
	student = get_object_or_404(Student, pk=pk)
	return render(request, 'main/students_open.html', {'student': student})

def task(request):
	tasks_list = Task.objects.all()
	return render(request, 'main/task.html', {'tasks_list': tasks_list})

def answer(request):
    if request.method == 'POST':
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            answer_form.save()
            return redirect('main')
    else:
        answer_form = AnswerForm()
    return render(request,
                  'main/answer.html',
                  {'task': task,
                   'answer_form': answer_form})

def main(request):
    return render(request, 'main/main.html')

def discipline(request):
    discipline_list = Discipline.objects.all()
    return render(request, 'main/discipline.html', {'discipline_list': discipline_list})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'main/logined_in.html')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

