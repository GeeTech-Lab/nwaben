from django.urls import re_path, path

from accounts.api.user.views import UserDetailAPIView

urlpatterns = [
    # re_path(r'^(?<username>\w+)/$', UserDetailAPIView.as_view(), name='detail'),
    path("<username>/", UserDetailAPIView.as_view(), name='detail'),
]