
from django.db import models

# Create your models here.



class Departments(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    head = models.CharField(max_length=255, verbose_name='Руководитель')
    staff_count = models.IntegerField(verbose_name='Численность')
    reports = models.ManyToManyField('Reports', verbose_name='Отчеты', blank=True)
    def __str__(self):
        return self.name

class Employees(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    position = models.ForeignKey('Positions', on_delete=models.CASCADE, verbose_name='Должность', null=True, blank=True)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, verbose_name='Отдел', related_name='employees', null=True, blank=True)
    reports = models.ManyToManyField('Reports', verbose_name='Отчеты', blank=True)
    salary = models.IntegerField(verbose_name='Зарплата', blank=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Positions(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    min_salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Минимальная зарплата')
    def __str__(self):
        return self.name

class Reports(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    creator = models.ForeignKey(Employees, on_delete=models.CASCADE, verbose_name='Создатель', related_name='created_reports')
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, verbose_name='Отдел', related_name='department_reports')
    description = models.TextField(verbose_name='Описание')




