# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.views.generic import UpdateView, CreateView, DeleteView
from django.db.models.deletion import ProtectedError
from django.http import HttpResponse, HttpResponseRedirect

from ..models.group import Group

# Views for Groups

def groups_list(request):
    groups = Group.objects.all()

    # try to order groups list
    order_by = request.GET.get('order_by', '')
    if order_by in ('title', 'leader'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()

    # paginate groups
    numb_pages = 3

    paginator = Paginator(groups, numb_pages)
    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        groups = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        groups = paginator.page(paginator.num_pages)

    return render(request, 'students/groups_list.html', 
                  {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'students/group_confirm_delete.html'


    def get_success_url(self):
        return reverse('home')


    def post(self, request, *args, **kwargs):
        try:
            a = self.delete(request, *args, **kwargs)
            if a:
                messages.success(self.request, u'Група {} успішно видалена!'.
                                 format(self.get_object(queryset=None)))
            return a
        except ProtectedError:
            messages.error(self.request, u'Група {} має студентів, \
                             будь ласка, видаліть спочатку їх!'. \
                             format(self.get_object(queryset=None)))

            return HttpResponseRedirect(reverse('groups'))

