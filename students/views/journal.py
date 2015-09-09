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
         '2015-09-01': True,  
         '2015-09-02': True,  
         '2015-09-03': True,  
         '2015-09-04': True,  
         '2015-09-05': False,  
         '2015-09-06': True,  
         '2015-09-07': False,  
         },
        },
        {'id': 2,
         'name': u'Корост',
         'surname': u'Андрій',
         'date': {
         '2015-09-01': True,  
         '2015-09-02': True,  
         '2015-09-03': True,  
         '2015-09-04': True,  
         '2015-09-05': False,  
         '2015-09-06': True,  
         '2015-09-07': False,  
          },
        },
        {'id': 3,
         'name': u'Antony',
         'surname': u'Pad',
         'date': {
         '2015-09-01': True,  
         '2015-09-02': True,  
         '2015-09-03': True,  
         '2015-09-04': True,  
         '2015-09-05': False,  
         '2015-09-06': True,  
         '2015-09-07': False,  
          },
        },
    )
    return render(request, 'students/journal.html',
                  {'journal_list': journal_list})
