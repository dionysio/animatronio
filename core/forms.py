from django import forms
from django.utils.translation import ugettext_lazy as _


class ContactForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"placeholder": _('Your email address'), "class": "form-control"}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={"placeholder": _('Hello Animatronio, ...'), "class": "form-control"}))

