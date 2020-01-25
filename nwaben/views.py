from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import FormView
from nwaben import email_settings
from nwaben.forms import ContactForm


class ContactView(SuccessMessageMixin, FormView):
    form_class = ContactForm
    template_name = 'about.html'
    success_url = reverse_lazy('about')
    success_message = 'Message sent successfully'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        message = form.cleaned_data['message']
        subject = 'Contact email recieved from www.nwaben.com'
        send_message = 'name: {} \n message: {} \n mobile: {}'.format(name, message, phone)
        from_email = form.cleaned_data['email']
        recipient_list = [email_settings.EMAIL_HOST_USER]
        send_mail(subject, send_message, from_email, recipient_list, fail_silently=False)
        return super(ContactView, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Message sent successfully!"