# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models import Student, Group

# Views for Students

def students_list(request):
    students = Student.objects.all()

    # try to order students list
    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    # paginate students
    paginator = Paginator(students, 3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        students = paginator.page(paginator.num_pages)

    return render(request, 'students/students_list.html',
                {'students': students})

def students_add(request):
    # Якщо форма була запощена:

        # Якщо кнопка Скасувати була натиснута:

            # Повертаємо користувача до списку студентів

        # Якщо кнопка Додати була натиснута:

            # Перевіряємо дані на коректність та збираємо помилки

            # Якщо дані були введені некоректно:
                # Віддаємо шаблон форми разом із знайденими помилками

            # Якщо дані були введені коректно:
                # Створюємо та зберігаємо студента в базу

            # Повертаємо користувача до списку студентів

    # Якщо форма не була запощена:
        # повертаємо код початкового стану форми

    return render(request, 'students/students_add.html', 
                  {'groups': Group.objects.all().order_by('title')})

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

