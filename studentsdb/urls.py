"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views.students. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.students.home, name='home')
Class-based views
    1. Add an import:  from other_app.views.students.import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url

from django.contrib import admin

from .settings import MEDIA_ROOT, DEBUG

from students.views.contact_admin import ContactAdminView, SuccessSentView
from students.views.students import StudentUpdateView, StudentCreateView, \
                                    StudentDeleteView

from students.views.groups import GroupDeleteView

urlpatterns = patterns('',

    # Students urls
    url(r'^$', 'students.views.students.students_list', name='home'),

    url(r'^students/add/$',
        StudentCreateView.as_view(),
        name='students_add'),

    url(r'^students/(?P<pk>\d+)/edit/$',
        StudentUpdateView.as_view(),
        name='students_edit'),

    url(r'^students/(?P<pk>\d+)/delete/$',
        StudentDeleteView.as_view(),
        name='students_delete'),

    # Groups urls

    url(r'^groups$', 'students.views.groups.groups_list',
        name='groups'),
    url(r'^groups/add/$', 'students.views.groups.groups_add',
        name='groups_add'),
    url(r'^groups/(?P<pk>\d+)/edit/$', 'students.views.groups.groups_edit',
        name='groups_edit'),
    url(r'^groups/(?P<pk>\d+)/delete/$',
        GroupDeleteView.as_view(),
        name='groups_delete'),

    # Journal urls

    url(r'^journal$', 'students.views.journal.journal',
        name='journal'),

    url(r'^contact_admin/',
        ContactAdminView.as_view(),
        name="contact_admin"),

    url(r'^contact_admin_sent/$',
        SuccessSentView.as_view(),
        name='contact_admin_sent'),

    url(r'^admin/', include(admin.site.urls)),

    # simple captcha
    url(r'^captcha/', include('captcha.urls')),

)

if DEBUG:
    # serve files from media folder
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': MEDIA_ROOT}))
