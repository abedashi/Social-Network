# Generated by Django 4.0.5 on 2022-09-30 22:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0008_alter_posts_datetime_alter_user_backgroundcolor'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 30, 22, 52, 39, 72602)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 30, 22, 52, 39, 72461)),
        ),
    ]
