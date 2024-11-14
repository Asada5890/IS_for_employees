from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from app.forms import *
from app.models import Employees
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User




def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active and user.check_password(cd['password']):
                    login(request, user)
                    return redirect('home')
                else:
                    return HttpResponse('Неправильный пароль')
            else:
                return HttpResponse('Такого пользователя не существует')
        else:
            return HttpResponse('Неправильный логин или пароль')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def home(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.save()  
            return redirect('/')  
    else:
        form = EmployeeForm()

    employees = Employees.objects.all()

    return render(request, 'index.html', {'form': form, 'employees': employees})









def employee_edit(request, employee_id):
    employee = get_object_or_404(Employees, id=employee_id)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()  
            return redirect('/')  
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'employee_edit.html', {'form': form, 'employee': employee})



def employee_delete(request, employee_id):
    employee = get_object_or_404(Employees, id=employee_id)
    
    if request.method == 'POST':
        employee.delete()   
        return redirect('/')  

    return render(request, 'employee_confirm_delete.html', {'employee': employee})