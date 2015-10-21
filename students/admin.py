# -*- coding: utf-8 -*-
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.forms import ModelForm, ValidationError

from .models import Student, Group
from .models.monthjournal import MonthJournal

class StudentFormAdmin(ModelForm):
    def clean_student_group(self):
        """Check if student is leader in any group.
        If yes, then ensure it's the same as selected group."""

        # get group where current student is a leader
        groups = Group.objects.filter(leader=self.instance)

        if len(groups) > 0 and self.cleaned_data['student_group'] != groups[0]:
            raise ValidationError(u'Студент є старостою іншої групи!', \
            code='invalid')

        return self.cleaned_data['student_group']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'ticket', 'student_group']
    list_display_links = ['last_name', 'first_name']
    list_editable = ['student_group']
    ordering = ['last_name']
    list_filter = ['student_group']
    list_per_page = 10
    search_fields = ['last_name', 'first_name', 
                     'middle_name', 'ticket', 'notes']

    actions = ['make_copy']
    form =  StudentFormAdmin

    def view_on_site(self, obj):
        return reverse('students_edit', kwargs={'pk': obj.id})

    def make_copy(self, request, queryset):
        for object in queryset:
            object.id = None
            object.save()
    make_copy.short_description = u"Скопіювати вибраних студентів"


class GroupFormAdmin(ModelForm):
    def clean_leader(self):
        """Check if leader is this group member."""

        # get group which this student belongs to
        student = self.instance.leader
        #self.instance.id
        if student.student_group != self.instance:
            raise ValidationError(u'Студент належить до іншої групи!', \
            code='invalid')

        return self.cleaned_data['leader']


class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'leader', 'notes']
    list_display_links = ['title']
    list_editable = ['leader']
    ordering = ['title']
    list_per_page = 10
    search_fields = ['title', 'leader', 
                     'notes']
    form =  GroupFormAdmin

    def view_on_site(self, obj):
        return reverse('groups_edit', kwargs={'pk': obj.id})


# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(MonthJournal)
