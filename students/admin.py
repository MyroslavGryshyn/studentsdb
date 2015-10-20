from django.contrib import admin
from django.core.urlresolvers import reverse

from .models import Student, Group
from .models.monthjournal import MonthJournal

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

    def view_on_site(self, obj):
        return reverse('students_edit', kwargs={'pk': obj.id})

    def make_copy(self, request, queryset):
        for object in queryset:
            object.id = None
            object.save()
    make_copy.short_description = "Make copy of checked students"

class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'leader', 'notes']
    list_display_links = ['title']
    list_editable = ['leader']
    ordering = ['title']
    list_per_page = 10
    search_fields = ['title', 'leader', 
                     'notes']

    def view_on_site(self, obj):
        return reverse('groups_edit', kwargs={'pk': obj.id})


# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(MonthJournal)
