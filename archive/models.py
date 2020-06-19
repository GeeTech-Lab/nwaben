# from audiofield.fields import AudioField
from cloudinary.models import CloudinaryField
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


def upload_dir(instance, filename):
    return "{}/{}".format(instance.author, filename)


class Album(models.Model):
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    artist = models.CharField(max_length=250)
    album_name = models.CharField(max_length=500)
    slug = models.SlugField(max_length=255, unique=True, null=False)
    genre = models.CharField(max_length=100)
    price = models.PositiveIntegerField(blank=True, null=True)
    album_logo = CloudinaryField(upload_dir, blank=True)
    date_uploaded = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Archives"
        ordering = ('date_uploaded',)
        unique_together = ["artist", "album_name", ]

    def __str__(self):
        return self.album_name

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'slug': self.slug})

    @property
    def image_url(self):
        if self.album_logo:
            return self.album_logo.url
        return 'https://res.cloudinary.com/geetechlab-com/image/upload/v1580824596/nwaben.com/blog_image1_eklmqy.jpg'

    def album_songs(self):
        album = Album.objects.get(slug=self.slug)
        return album.song_set.count()


def album_pre_save_signal(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.album_name)
        new_slug = "{}-{}".format(instance.album_name, instance.id)
        try:
            instance.slug = slugify(new_slug)
        except Album.DoesNotExist:
            instance.slug = instance.slug
        except Album.MultipleObjectsReturned:
            instance.slug = slugify(new_slug)
        except:
            pass


pre_save.connect(album_pre_save_signal, sender=Album)


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, unique=True, null=False)
    # audio_file = AudioField(upload_dir, blank=True, ext_whitelist=(".mp3", ".wav", ".ogg"),
    #                         help_text="Allowed type - .mp3, .wav, .ogg")
    audio_file = CloudinaryField(upload_dir, blank=True)
    track_number = models.IntegerField()

    def __str__(self):
        return self.song_title


# # Add this method to your model
# def audio_file_player(self):
#     """audio player tag for admin"""
#     if self.audio_file:
#         file_url = settings.MEDIA_URL + str(self.audio_file)
#         player_string = '<audio src="{}" controls>Your browser does not support the audio element.</audio>'.format(
#             file_url)
#         return player_string
#
#
# audio_file_player.allow_tags = True
# audio_file_player.short_description = 'Audio file player'


def song_pre_save_signal(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.song_title)
        new_slug = "{}-{}".format(instance.song_title, instance.id)
        try:
            instance.slug = slugify(new_slug)
        except Album.DoesNotExist:
            instance.slug = instance.slug
        except Album.MultipleObjectsReturned:
            instance.slug = slugify(new_slug)
        except:
            pass


pre_save.connect(song_pre_save_signal, sender=Song)
