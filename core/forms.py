from django import forms
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    name = forms.CharField(label=_('Name'), max_length=100)
    email = forms.EmailField(
        label=_('Email'),
        max_length=100,
        validators=[EmailValidator]
    )
    subject = forms.CharField(label=_('Subject'), max_length=100)
    message = forms.CharField(label=_('Message'), widget=forms.Textarea)
    captcha = CaptchaField()
