import os
import sendgrid
from django.contrib.sites import requests
from nwaben.settings import BASE_DIR


#=======use this settings if you are on developer mode======
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
# EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")


#=======use this settings if you are on production mode======
SENDGRID_API_KEY = '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 '
EMAIL_HOST = 'stmp.sendgrid.net'
EMAIL_HOST_USER = 'app156328640@heroku.com'
EMAIL_HOST_PASSWORD = 'Gerard007'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = 'geetechlab@gmail.com'
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'Contact email recieved from nwaben.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

