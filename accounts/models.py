import random
import os

from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.db.models.signals import pre_save
from phonenumber_field.modelfields import PhoneNumberField

from nwaben.utils import unique_slug_generator

User = get_user_model()
GENDER_CHOICE = (("M", "Male"), ("F", "Female"))

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1, 191092013)
    name, ext = get_filename_ext(filename)
    final_filename = "{}{}".format(new_filename=new_filename, ext=ext)
    return "profile/{}/{}".format(new_filename=new_filename, ext=ext)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    phone = PhoneNumberField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE, blank=True, null=True)
    image = CloudinaryField(upload_image_path, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'profile'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        unique_together = ('phone', 'slug')

    def __str__(self):
        return str(self.user.username)

    def image_tag(self):
        from django.utils.safestring import mark_safe
        return mark_safe('<img src="{}" width="100" height="100"/>'.format(self.image.url))
    image_tag.short_description='Profile Image'
    image_tag.allow_tags = True


def post_save_profile_reciever(sender, instance, created, *args, **kwargs):
    if created:
        if not instance.slug:
            instance.slug = unique_slug_generator(instance)

pre_save.connect(post_save_profile_reciever, sender=Profile)