# Generated by Django 2.2 on 2021-02-10 10:59

import articles.models
from django.db import migrations, models
import nwaben.storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=nwaben.storage_backends.PublicMediaStorage(), upload_to=articles.models.upload_dir),
        ),
    ]