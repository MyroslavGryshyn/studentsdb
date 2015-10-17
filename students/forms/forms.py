# -*- coding: utf-8 -*-

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from captcha.fields import CaptchaField

from contact_form.forms import ContactForm

from django import forms
from django.core.urlresolvers import reverse

from collections import OrderedDict
from django.contrib import messages

from django.core.mail import send_mail

class ContactAdmin(ContactForm):

    # style for form
    def __init__(self, request=None, *args, **kwargs):

        # call original initializer
        super(ContactAdmin, self).__init__(request=request, *args, **kwargs)

        # this helper object allow us to customize form
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
        self.helper.add_input(Submit('send_button', ('Submit'),
                                     css_class='btn-primary'))

        #Ordering our form
        fields_keyOrder = ['subject', 'email', 'body']

        if (self.fields.has_key('keyOrder')):
            self.fields.keyOrder = fields_keyOrder
        else:
            self.fields = \
                OrderedDict((k, self.fields[k]) for k in fields_keyOrder)

    email = forms.EmailField(
        label=u"Ваша Емейл Адреса")

    subject = forms.CharField(
        label=u"Тема листа",
        required=False,
        max_length=128)

    body = forms.CharField(
        label=u"Текст повідомлення",
        widget=forms.Textarea)


    def save(self, fail_silently=False):

        error_message = ('When you send a letter to an unexpected error occurred. Please try again later')
        success_message = ('The message has been successfully sent')

        try:
            send_mail(fail_silently=True, **self.get_message_dict())

        except Exception:
            messages.error(self.request, error_message)

        else:
            messages.success(self.request, success_message)
    

