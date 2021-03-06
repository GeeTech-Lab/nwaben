# Generated by Django 2.2 on 2021-02-10 10:59

import accounts.models
from django.db import migrations, models
import nwaben.storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210210_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, help_text='You profile image', null=True, storage=nwaben.storage_backends.PublicMediaStorage(), upload_to=accounts.models.upload_dir),
        ),
    ]
