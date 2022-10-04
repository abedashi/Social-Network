# Generated by Django 4.0.5 on 2022-10-04 00:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0009_comments_datetime_alter_posts_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(default='No Bio'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 4, 0, 23, 52, 126711)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 4, 0, 23, 52, 126566)),
        ),
    ]
