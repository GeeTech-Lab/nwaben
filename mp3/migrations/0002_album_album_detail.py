# Generated by Django 2.2 on 2021-02-10 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp3', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_detail',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
