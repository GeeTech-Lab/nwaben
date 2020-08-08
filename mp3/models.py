# from audiofield.fields import AudioField
from cloudinary.models import CloudinaryField
from cloudinary.templatetags import cloudinary
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.http import request
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

from .utils import random_key_generator, reference_id
# from .validators import validate_file_extension


def upload_dir(instance, filename):
    return "{}/{}".format(instance.uploaded_by, filename)
    # return cloudinary.uploader.upload(request.FILES['file'])


class Album(models.Model):
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    artist = models.CharField(max_length=250)
    album_name = models.CharField(max_length=255)
    album_token = models.CharField(blank=True, null=True, max_length=20)
    slug = models.SlugField()
    genre = models.CharField(max_length=100)
    album_logo = CloudinaryField(upload_dir, blank=True, null=True)
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
        return 'https://res.cloudinary.com/geetechlab-com/image/upload/v1580824596/nwaben.com/blog_image1_eklmqy.jpg'

    def album_songs(self):
        album_obj = Album.objects.get(slug=self.slug)
        return album_obj.song_set.count()

    # def save(self, *args, **kwargs):
    #     original_slug = slugify(self.album_name)
    #     queryset = Album.objects.filter(slug__iexact=original_slug).count()
    #     count = 1
    #     slug = original_slug
    #     while queryset:
    #         slug = original_slug + '-' + str(count)
    #         count += 1
    #         queryset = Album.objects.filter(slug__iexact=original_slug).count()
    #     self.slug = slug
    #     self.album_token = random_key_generator(self.slug)


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
    song_token = models.CharField(max_length=225)
    song_title = models.CharField(max_length=225)
    slug = models.SlugField()
    price = models.PositiveIntegerField(blank=True, null=True)
    paid = models.BooleanField(default=False)
    song_url = models.URLField(blank=True, null=True, max_length = 200)
    # song_url = models.CharField(max_length=255, blank=True, null=True)
    # audio_file = models.CloudinaryField()

    class Meta:
        verbose_name = 'Song'
        verbose_name_plural = 'Songs'

    def __str__(self):
        return "{}".format(self.song_title)

    def get_absolute_url(self):
        return reverse('mp3:album_detail', kwargs={'slug': self.slug})

    @property
    def initiated_payment(self):
        return reference_id()

    @property
    def payment_success(self):
        self.paid = True
        return self.paid

    # def save(self, *args, **kwargs):
    #     original_slug = slugify(self.song_title)
    #     queryset = Song.objects.filter(slug__iexact=original_slug).count()
    #     count = 1
    #     slug = original_slug
    #     while queryset:
    #         slug = original_slug + '-' + str(count)
    #         count += 1
    #         queryset = Song.objects.filter(slug__iexact=original_slug).count()
    #     self.slug = slug


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
