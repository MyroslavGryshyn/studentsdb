# -*- coding: utf-8 -*-
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import UpdateView, CreateView, DeleteView
import imghdr
from django.contrib import messages

from ..models import Student, Group
from ..forms.forms import StudentUpdateForm, StudentCreateForm


#Class based views for Students
class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/students_form.html'
    form_class = StudentUpdateForm

    def get_success_url(self):
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.error(request, u'Ви відмінили редагування студента')
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.success(request, u'Студента успішно збережено!')
            return super(StudentUpdateView, self).post(request, *args, **kwargs)


class StudentCreateView(CreateView):
    model = Student
    template_name = 'students/students_form.html'
    form_class = StudentCreateForm

    def get_success_url(self):
        return reverse('home')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.error(request, u'Ви відмінили додавання студента')
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.success(request, u'Студента успішно збережено!')
            return super(StudentCreateView, self).post(request, *args, **kwargs)


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/students_confirm_delete.html'


    def get_success_url(self):
        messages.success(self.request, u'Студента {} успішно видалено!'. \
                         format(self.get_object(queryset=None)))
        return reverse('home')


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
    paginator = Paginator(students, 5)
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

