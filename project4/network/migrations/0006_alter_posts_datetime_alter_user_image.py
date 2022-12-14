# Generated by Django 4.0.5 on 2022-09-28 13:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_user_backgroundcolor_user_image_alter_posts_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 28, 13, 16, 31, 414043)),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='profile.png', null=True, upload_to='images'),
        ),
    ]
