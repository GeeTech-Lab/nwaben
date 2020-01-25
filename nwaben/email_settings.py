import os

from django.contrib.sites import requests

from nwaben.settings import BASE_DIR

#=======use this settings if you are on developer mode======
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
# EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")

#=======use this settings if you are on production mode======
SENDGRID_API_KEY = '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'
EMAIL_HOST = 'stmp.sendgrid.net'
EMAIL_HOST_USER = 'app156328640@heroku.com'
EMAIL_HOST_PASSWORD = 'Gerard007'
EMAIL_PORT = '25'
EMAIL_USE_TLS = True
# EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = 'geetechlab@gmail.com'
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'Contact email recieved from nwaben.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


# def send_simple_message():
# 	return requests.post(
# 		"https://api.mailgun.net/v3/sandbox84594d9f1b8d45d3804ef224cc2d22c4.mailgun.org/messages",
# 		auth=("api", "9d31fe4e8a8992082902ac5d5576f563-9dfbeecd-d74faceb"),
# 		data={"from": "Mailgun Sandbox <postmaster@sandbox84594d9f1b8d45d3804ef224cc2d22c4.mailgun.org>",
# 			"to": "GeeTech Lab <geetechlab@gmail.com>",
# 			"subject": "Hello GeeTech Lab",
# 			"text": "Congratulations GeeTech Lab, you just sent an email with Mailgun!  You are truly awesome!"})
#
# # You can see a record of this email in your logs: https://app.mailgun.com/app/logs.
# # You can send up to 300 emails/day from this sandbox server.
# # Next, you should add your own domain so you can send 10000 emails/month for free.


SEND_GRID_API_KEY = os.environ.get("SEND_GRID_API_KEY", '')
EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_HOST = 'mail.musicadence.com'
EMAIL_HOST_USER = 'info@nwaben.com'
EMAIL_HOST_PASSWORD = 'Gerard@007'
EMAIL_PORT = '25'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'info@nwaben.com'
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'Contact email recieved from nwaben.com'