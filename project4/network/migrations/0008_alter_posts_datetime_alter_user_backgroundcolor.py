# Generated by Django 4.0.5 on 2022-09-29 16:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_alter_posts_datetime_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 29, 16, 41, 31, 73852)),
        ),
        migrations.AlterField(
            model_name='user',
            name='backgroundColor',
            field=models.TextField(default='#cb444a'),
        ),
    ]
