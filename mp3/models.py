from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from django.utils.text import slugify

from nwaben.storage_backends import PrivateMediaStorage, PublicMediaStorage
from .validators import validate_file_extension


class Album(models.Model):
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    artist = models.CharField(max_length=250)
    album_name = models.CharField(max_length=255)
    slug = models.SlugField()
    owned_by = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                      blank=True, related_name='owned_by')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    genre = models.CharField(max_length=100)
    album_logo = models.ImageField(upload_to='album/covers', blank=True, null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Albums"
        ordering = ('date_uploaded',)
        unique_together = ["album_name"]

    def __str__(self):
        return "{}".format(self.album_name)

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


# def album_post_save_signal(instance, *args, **kwargs):
#     if instance.uploaded_by:
#         instance.owned_by.add(instance.uploaded_by)
#
#
# post_save.connect(album_post_save_signal, sender=Album)


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


pre_save.connect(album_pre_save_signal, sender=Album)


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=225)
    slug = models.SlugField()
    audio_file = models.FileField(storage=PublicMediaStorage(),
                                  upload_to='album/songs',
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
        except Song.DoesNotExist:
            instance.slug = instance.slug
        except Song.MultipleObjectsReturned:
            instance.slug = slugify(new_slug)
    # elif not instance.song_token:
    #     instance.song_token = instance.album.album_token


pre_save.connect(song_pre_save_signal, sender=Song)
