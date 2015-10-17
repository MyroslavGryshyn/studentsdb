# -*- coding: utf-8 -*-
from django.views.generic import TemplateView

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib import messages

from contact_form.views import ContactFormView
from django.views.generic.base import RedirectView
from django.http import HttpResponse

from ..forms.forms import ContactAdmin

class ContactAdminView(ContactFormView):
    form_class = ContactAdmin

    def get_success_url(self):
        return reverse('contact_admin_sent')

class SuccessSentView(TemplateView):
    template_name = 'contact_form/contact_admin_sent.html'


