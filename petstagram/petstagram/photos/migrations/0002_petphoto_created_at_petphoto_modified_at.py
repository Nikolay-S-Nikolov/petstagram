# Generated by Django 5.1 on 2024-08-21 17:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='petphoto',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='petphoto',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
