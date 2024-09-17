# Generated by Django 5.1 on 2024-08-21 18:32

import petstagram.photos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_alter_petphoto_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petphoto',
            name='photo',
            field=models.ImageField(upload_to='pet_photos/', validators=[petstagram.photos.models.ImageSizeValidator(5242880)]),
        ),
    ]