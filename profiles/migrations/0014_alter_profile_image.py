# Generated by Django 3.2.20 on 2023-09-16 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default-user-image.png', upload_to='images/'),
        ),
    ]