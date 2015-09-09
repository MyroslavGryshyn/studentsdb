# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

# Views for Journal 

def journal(request):
    journal_list = (
        {'id': 1,
         'name': u'Віталій',
         'surname': u'Подоба',
         'date': {
         u'Mn 1': True,  
         u'Mn 2': True,  
         u'Mn 3': True,  
         u'Mn 4': True,  
         u'Mn 5': False,  
         u'Mn 6': True,  
         u'Mn 7': False,  
         u'Mn 8': True,  
         u'Mn 9': True,  
         u'Mn 11': True,  
         u'Mn 12': True,  
         u'Mn 13': False,  
         },
        },
        {'id': 2,
         'name': u'Корост',
         'surname': u'Андрій',
         'date': {
         u'Пн 1': True,  
         u'Вт 2': True,  
         u'Вт 3': True,  
         u'Вт 4': True,  
         u'Вт 5': False,  
         u'Вт 6': True,  
         u'Вт 7': False,  
         u'Вт 8': True,  
         u'Вт 9': True,  
         u'Вт 11': True,  
         u'Вт 12': True,  
         u'Вт 13': False,  
         },
        },
        {'id': 3,
         'name': u'Antony',
         'surname': u'Pad',
         'date': {
         u'Пн 1': True,  
         u'Вт 2': True,  
         u'Вт 3': True,  
         u'Вт 4': True,  
         u'Вт 5': False,  
         u'Вт 6': True,  
         u'Вт 7': False,  
         u'Вт 8': True,  
         u'Вт 9': True,  
         u'Вт 11': True,  
         u'Вт 12': True,  
         u'Вт 13': False,  
          },
        },
    )
    return render(request, 'students/journal.html',
                  {'journal_list': sorted(journal_list)})
