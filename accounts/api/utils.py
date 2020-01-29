import datetime
from django.conf import settings
from rest_framework_jwt.settings import api_settings

expire_delta=api_settings.JWT_REFRESH_EXPIRATION_DELTA

def jwt_response_payload_handler(token, user=None, password=None, request=None):
    return {
        'token': token,
        'user': user.username,
        'password': password,
        'expires': datetime.timezone.now() + expire_delta - datetime.timedelta(seconds=200)
    }