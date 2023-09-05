# Generated by Django 3.2.20 on 2023-09-04 14:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reading_list', '0002_auto_20230904_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='users_temp',
        ),
        migrations.AddField(
            model_name='book',
            name='users',
            field=models.ManyToManyField(related_name='reading_list', through='reading_list.UserBook', to=settings.AUTH_USER_MODEL),
        ),
    ]
