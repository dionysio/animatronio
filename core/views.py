import django.views.generic as views
from django.utils.decorators import method_decorator
from django.conf import settings
from django.core.mail import EmailMessage
from django.contrib import messages
from django.utils.translation import ugettext as _
import smtplib

from honeypot.decorators import check_honeypot
from . import forms, models


class HomeView(views.ListView):
    model = models.TaggedPicture
    context_object_name = 'pictures'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = forms.ContactForm()
        return context

    def get_queryset(self):
        return self.model.objects.prefetch_related('tags')


class Contact(views.FormView):
    form_class = forms.ContactForm
    success_url = '/'
    http_method_names = ['post']

    @method_decorator(check_honeypot)
    def dispatch(self, *args , **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        admin_mail = settings.ADMINS[0][1]
        try:
            email = EmailMessage(
                _('Message from Animatronio site'),
                form.cleaned_data['message'],
                settings.SERVER_EMAIL,
                [admin_mail],
                reply_to=[form.cleaned_data['email']]
            )
            email.send()
            messages.success(self.request, _('My human assistant will handle your message.'))
        except (smtplib.SMTPException, ConnectionRefusedError):
            messages.error(self.request, _('I tried my damn hardest to forward your message to my human assistant, but I could not. Please contact him at {}'.format(admin_mail)))
            pass
        return super().form_valid(form)