# def contact(request):
#     form = ContactForm(request.POST or None)
#
#     if form.is_valid():
#         name = form.cleaned_data['name']
#         phone = form.cleaned_data['phone']
#         message = form.cleaned_data['message']
#         # send_mail(subject, send_message, from_email, recipient_list, fail_silently=True)
#         sg_message = Mail(
#             from_email = form.cleaned_data['email'],
#             to_emails = [email_settings.EMAIL_HOST_USER],
#             subject = 'Contact email recieved from www.nwaben.com',
#             html_content = 'name: {} \n message: {} \n mobile: {}'.format(name, message, phone)
#         )
#         sg = SendGridAPIClient(email_settings.SENDGRID_API_KEY)
#         sg.send(sg_message)
#         # response = sg.send(sg_message)
#         messages.success(request, 'Your message was sent successfully!')
#         form = None
#
#     context = {'form': form}
#     template = 'about.html'
#     return render(request, template, context)


#def form_valid(self, form):
#         name = form.cleaned_data['name']
#         phone = form.cleaned_data['phone']
#         message = form.cleaned_data['message']
#         subject = 'Contact email recieved from www.nwaben.com'
#         send_message = 'name: {} \n message: {} \n mobile: {}'.format(name, message, phone)
#         from_email = form.cleaned_data['email']
#         recipient_list = [email_settings.EMAIL_HOST_USER]
#         send_mail(subject, send_message, from_email, recipient_list, fail_silently=False)
#         return super(ContactView, self).form_valid(form)