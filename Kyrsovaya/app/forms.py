from app.models import Employees
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ('first_name', 'last_name', 'position', 'salary', 'department')



class LoginForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль')



class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль')
    password2 = forms.CharField(label='Повторите пароль')
    username = forms.CharField(label='Логин')
    first_name = forms.CharField(label='Ваше имя')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'password')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('пароли не совпадают.')
        return cd['password2']