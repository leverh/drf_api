# Generated by Django 3.2.20 on 2023-09-16 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='v1694521251/Windows_10_Default_Profile_Picture.svg_lydzzy.png', upload_to='images/'),
        ),
    ]