# Generated by Django 4.0.5 on 2022-09-05 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='followID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='network.follows'),
        ),
    ]