from django.contrib.auth import get_user_model
from rest_framework import generics

from accounts.api.user.serializers import UserDetailSerializer

User = get_user_model()

class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.Objects.filter(is_active=True)
    serializer_class = UserDetailSerializer
    lookup_field = 'username'

    def get_serializer_context(self):
        return {'request': self.request}