# -*- coding: utf-8 -*-
from django.shortcuts import render
from django import forms

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from studentsdb.settings import ADMIN_EMAIL
from django.contrib import messages

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        # call original initializator
        super(ContactForm, self).__init__(*args, **kwargs)

        # this helper object allows us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('contact_admin')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # form buttons
        self.helper.add_input(Submit('send_button', u'Надіслати'))


    from_email = forms.EmailField(
        label=u"Ваша Емейл Адреса",
        error_messages={'required': 
                        u'Будь ласка, введіть свій email'},
    )

    subject = forms.CharField(
        label=u"Заголовок листа",
        required=False,
        max_length=128)

    message = forms.CharField(
        label=u"Текст повідомлення",
        max_length=2560,
        error_messages={'required': 
                        u'Будь ласка, заповніть поле повідомлення'},
        widget=forms.Textarea)

def contact_admin(request):
    # check if form was posted
    if request.method == 'POST':
    # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)

    # check whether user data is valid:
        if form.is_valid():
            # send email
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']

            try:
                send_mail(subject, message, from_email, [ADMIN_EMAIL])

            except Exception:
                messages.error(request, u"""Під час відправки листа виникла непередбачувана 
                помилка. Спробуйте скористатись даною формою пізніше.""")

            else:
                messages.success(request, u'Повідомлення успішно надіслане!')

            return HttpResponseRedirect(reverse('contact_admin'))
                          
        else:
            return render(request, 'contact_admin/form.html', 
                          {'form': form})

    # if there was not POST render blank form
    else:
        form = ContactForm()
        return render(request, 'contact_admin/form.html', 
                      {'form': form})

