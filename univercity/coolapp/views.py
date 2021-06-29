from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import (Faculty,
                     Direction,
                     Subject,
                     Teacher,
                     Group,
                     Student
                     )
from .forms import FacultyForm, DirectionForm, SubjectForm, TeacherForm, GroupForm, StudentForm

def login_required_decorator(func):
    return login_required(func)

def login_page(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home_page')
    return render(request, 'login.html')

@login_required_decorator
def login_out(request):
    logout(request)
    return redirect('login_page')

@login_required_decorator
def index_page(request):
    return render(request, 'index.html')


@login_required_decorator
def faculty_list(request):
    faculties = Faculty.objects.all()
    ctx = {
        'faculties': faculties
    }
    return render(request, 'faculty/list.html', ctx)

@login_required_decorator
def faculty_create(request):
    form = FacultyForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()
        return redirect('faculty_list')
    ctx = {
        'form': form
    }
    return render(request, 'faculty/form.html', ctx)

@login_required_decorator
def faculty_edit(request, pk):
    model = Faculty.objects.get(id=pk)
    form = FacultyForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('faculty_list')
    ctx = {
        'model': model,
        'form': form,
    }
    return render(request, 'faculty/form.html', ctx)

@login_required_decorator
def faculty_delete(request, pk):
    model = Faculty.objects.get(id=pk)
    model.delete()
    return redirect('faculty_list')



@login_required_decorator
def direction_list(request):
    directions = Direction.objects.all()
    ctx = { 'directions': directions }
    return render(request, 'direction/list.html', ctx)

@login_required_decorator
def direction_create(request):
    form = DirectionForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()
        return redirect('direction_list')
    ctx = {'form': form}
    return render(request, 'direction/form.html', ctx)

@login_required_decorator
def direction_edit(request, pk):
    model = Direction.objects.get(id=pk)
    form = DirectionForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('direction_list')
    ctx = {
        'model':model,
        'form': form
    }
    return render(request, 'direction/form.html', ctx)

@login_required_decorator
def direction_delete(request, pk):
    model = Direction.objects.get(id=pk)
    model.delete()
    return redirect('direction_list')


@login_required_decorator
def subject_list(request):
    subjects = Subject.objects.all()
    ctx = { 'subjects': subjects }
    return render(request, 'subject/list.html', ctx)

@login_required_decorator
def subject_create(request):
    form = SubjectForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()
        return redirect('subject_list')
    ctx = {'form': form}
    return render(request, 'subject/form.html', ctx)

@login_required_decorator
def subject_edit(request, pk):
    model = Subject.objects.get(id=pk)
    form = SubjectForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('subject_list')
    ctx = {
        'model':model,
        'form': form
    }
    return render(request, 'subject/form.html', ctx)

@login_required_decorator
def subject_delete(request, pk):
    model = Subject.objects.get(id=pk)
    model.delete()
    return redirect('subject_list')




@login_required_decorator
def teacher_list(request):
    teachers = Teacher.objects.all()
    ctx = { 'teachers': teachers }
    return render(request, 'teacher/list.html', ctx)

@login_required_decorator
def teacher_create(request):
    form = TeacherForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()
        return redirect('teacher_list')
    ctx = {'form': form}
    return render(request, 'teacher/form.html', ctx)

@login_required_decorator
def teacher_edit(request, pk):
    model = Teacher.objects.get(id=pk)
    form = TeacherForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('teacher_list')
    ctx = {
        'model':model,
        'form': form
    }
    return render(request, 'teacher/form.html', ctx)

@login_required_decorator
def teacher_delete(request, pk):
    model = Teacher.objects.get(id=pk)
    model.delete()
    return redirect('teacher_list')




@login_required_decorator
def group_list(request):
    groups = Group.objects.all()
    ctx = { 'groups': groups }
    return render(request, 'group/list.html', ctx)

@login_required_decorator
def group_create(request):
    form = GroupForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()
        return redirect('group_list')
    ctx = {'form': form}
    return render(request, 'group/form.html', ctx)

@login_required_decorator
def group_edit(request, pk):
    model = Group.objects.get(id=pk)
    form = GroupForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('group_list')
    ctx = {
        'model':model,
        'form': form
    }
    return render(request, 'group/form.html', ctx)

@login_required_decorator
def group_delete(request, pk):
    model = Group.objects.get(id=pk)
    model.delete()
    return redirect('group_list')



@login_required_decorator
def student_list(request):
    students = Student.objects.all()
    ctx = { 'students': students }
    return render(request, 'student/list.html', ctx)

@login_required_decorator
def student_create(request):
    form = StudentForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()
        return redirect('student_list')
    ctx = {'form': form}
    return render(request, 'student/form.html', ctx)

@login_required_decorator
def student_edit(request, pk):
    model = Student.objects.get(id=pk)
    form = StudentForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('student_list')
    ctx = {
        'model':model,
        'form': form
    }
    return render(request, 'student/form.html', ctx)

@login_required_decorator
def student_delete(request, pk):
    model = Student.objects.get(id=pk)
    model.delete()
    return redirect('student_list')