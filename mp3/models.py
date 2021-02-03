from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.http import request
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

from nwaben.storage_backends import PrivateMediaStorage, PublicMediaStorage
from .utils import random_key_generator, reference_id
from .validators import validate_file_extension


def upload_dir(instance, filename):
    return "{}/{}".format(instance.user.username, filename)


class Album(models.Model):
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    artist = models.CharField(max_length=250)
    album_name = models.CharField(max_length=255)
    album_token = models.CharField(blank=True, null=True, max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    paid = models.BooleanField(default=False)
    slug = models.SlugField()
    genre = models.CharField(max_length=100)
    album_logo = models.ImageField(upload_to=upload_dir, blank=True, null=True)
    date_uploaded = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Albums"
        ordering = ('date_uploaded',)
        unique_together = ["artist", "album_name"]

    def __str__(self):
        return "{}__{}".format(self.album_name, self.album_token)

    def get_absolute_url(self):
        return reverse('mp3:album_detail', kwargs={'slug': self.slug})

    @property
    def image_url(self):
        if self.album_logo:
            return self.album_logo.url
        return 'https://res.cloudinary.com/geetechlab-com/image/upload/c_scale,h_159,q_42/v1597153444/nfivbpcanbr8s6mjn2uy.png'

    def album_songs(self):
        album_obj = Album.objects.get(slug=self.slug)
        return album_obj.song_set.count()

    # @property
    # def initiated_payment(self):
    #     return reference_id()

    @property
    def payment_success(self):
        if self.album_token:
            self.paid = True
        return self.paid


def album_pre_save_signal(sender, instance, *args, **kwargs):
    if not instance.slug:
        new_slug = "{}-{}".format(instance.album_name, instance.artist)
        print(instance.pk)
        try:
            instance.slug = slugify(instance.album_name)
        except Album.DoesNotExist:
            instance.slug = instance.slug
        except Album.MultipleObjectsReturned:
            instance.slug = slugify(new_slug)
    elif not instance.album_token:
        instance.album_token = random_key_generator(instance.slug)


pre_save.connect(album_pre_save_signal, sender=Album)


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_token = models.CharField(max_length=225, blank=True, null=True)
    song_title = models.CharField(max_length=225)
    slug = models.SlugField()
    audio_file = models.FileField(storage=PublicMediaStorage(), upload_to=upload_dir,
                                  blank=True,
                                  null=True,
                                  max_length=200,
                                  validators=[validate_file_extension])

    class Meta:
        verbose_name = 'Song'
        verbose_name_plural = 'Songs'

    def __str__(self):
        return "{}".format(self.song_title)

    def get_absolute_url(self):
        return reverse('mp3:album_detail', kwargs={'slug': self.slug})


def song_pre_save_signal(sender, instance, *args, **kwargs):
    if not instance.slug:
        new_slug = "{}-{}".format(instance.song_title, instance.pk)
        try:
            instance.slug = slugify(instance.song_title)
        except Album.DoesNotExist:
            instance.slug = instance.slug
        except Album.MultipleObjectsReturned:
            instance.slug = slugify(new_slug)
    # elif not instance.song_token:
    #     instance.song_token = instance.album.album_token


pre_save.connect(song_pre_save_signal, sender=Song)
