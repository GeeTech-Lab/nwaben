from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)
from django.utils import timezone
from cloudinary.models import CloudinaryField


# default_path="https://res.cloudinary.com/hwz12fud7/image/upload/v1537132883/media/Gerard%20Nwazk/musicadence_fpdfvb.jpg"
from phonenumber_field.modelfields import PhoneNumberField

GENDER_CHOICE = (("Male", "Male"), ("Female", "Female"))


def upload_dir(instance, filename):
    return "{}/{}".format(instance.username, filename)


class UserManager(BaseUserManager):

    def create_user(self, email, username, phone=None, gender=None, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        elif not phone:
            raise ValueError('Pls provide your mobile number eg: +234080312345678')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone=phone,
            gender=gender,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, phone, gender, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            username,
            phone,
            gender,
            password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    bio = models.CharField(max_length=240, blank=True, default="")
    avatar = CloudinaryField(upload_dir, null=True, blank=True)
    phone = PhoneNumberField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICE, blank=True, null=True)
    follow_count = models.PositiveIntegerField(default=0)
    date_joined = models.DateTimeField(auto_now_add=True, )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username', 'phone', 'gender']

    def __str__(self):
        return "@{}".format(self.username)

    @property
    def image_url(self):
        if self.avatar:
            return self.avatar.url
        else:
            return 'https://res.cloudinary.com/geetechlab-com/image/upload/v1583147406/nwaben.com/user_azjdde_sd2oje' \
                   '.jpg '

    def get_full_name(self):
        # The user is identified by their
        return self.username

    def get_short_name(self):
        # The user is identified by their
        return "{} ({})".format(self.username, self.email)
