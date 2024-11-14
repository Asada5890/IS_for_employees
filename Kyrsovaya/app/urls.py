# app_employees/urls.py
from django.urls import path
from app.views import home, employee_edit, employee_delete, register,user_login

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('home/', home, name='home'),
    path('employee/edit/<int:employee_id>/', employee_edit, name='employee_edit'),  # Путь для редактирования
    path('employee/delete/<int:employee_id>/', employee_delete, name='employee_delete')
]