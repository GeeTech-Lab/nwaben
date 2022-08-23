from django.contrib.messages.views import SuccessMessageMixin
# from django.core.mail import send_mail
# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
# from django.contrib import messages
from accounts.models import User
from nwaben import email_settings
from nwaben.forms import ContactForm
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class ContactView(SuccessMessageMixin, FormView):
    form_class = ContactForm
    template_name = 'about.html'
    success_url = reverse_lazy('about')
    success_message = 'Message sent successfully'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        message = form.cleaned_data['message']
        recipient_list = [email_settings.DEFAULT_FROM_EMAIL, 'nwazuruokenwaben@gmail.com']
        sg_message = Mail(
            from_email=form.cleaned_data['email'],
            to_emails=recipient_list,
            subject=email_settings.ACCOUNT_EMAIL_SUBJECT_PREFIX,
            html_content='<html> <p>name: {}</p> <p>message: {}</p> <small>mobile: {}</small> </html>'.format(name, message, phone)
        )
        sg = SendGridAPIClient(email_settings.SENDGRID_API_KEY)
        sg.send(sg_message)
        return super(ContactView, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Message sent successfully!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["staff_users"] = User.objects.filter(is_superuser=True)
        return context

