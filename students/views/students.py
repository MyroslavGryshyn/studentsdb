# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from ..models import Student

# Views for Students

def students_list(request):
    students = Student.objects.all()

    # Ordering students list
    order_by = request.GET.get('order_by', '')

    if order_by in ('last_name', 'first_name', 'ticket', 'id'):
        students = students.order_by(order_by)

        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    #page - from template
    page = request.GET.get('page')
    # If page is not an integer, deliver first page.
    try:
        page = int(page)
    except (ValueError, TypeError):
        page = 1

    per_page = 2

    num_pages, remainder = divmod(len(students), per_page)
    number_of_pages = num_pages + 1 if remainder else num_pages

    if page < 1:
        page = 1
    elif page > number_of_pages and number_of_pages:
        page = number_of_pages

    students = students[((int(page)-1)*per_page):((int(page)-1)*per_page+per_page)]
                        
    return render(request, 'students/students_list.html', \
                  {'students': students,  \
                   'pages': [x for x in xrange(1, number_of_pages+1)], \
                   'page': page})

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

