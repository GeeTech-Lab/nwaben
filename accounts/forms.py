from .models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "phone", "gender", "password1", "password2")
        model = User

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({'placeholder': 'username'})
        self.fields["email"].widget.attrs.update({'placeholder': 'example@email.com'})
        self.fields["phone"].widget.attrs.update({'placeholder': '+234801234567'})
        self.fields["gender"].widget.attrs.update({'placeholder': 'select gender'})
        self.fields["password1"].widget.attrs.update({'placeholder': 'password'})
        self.fields["password2"].widget.attrs.update({'placeholder': 'confirm password'})

        self.fields["username"].label = ""
        self.fields["email"].label = ""
        self.fields["phone"].label = ""
        self.fields["gender"].label = ""
        self.fields["password1"].label = ""
        self.fields["password2"].label = ""
        self.fields["password1"].help_text = ""
        self.fields["password2"].help_text = ""


class UserChangeForm(UserChangeForm):
    class Meta:
        fields = ("avatar", "bio", "phone")
        model = User
