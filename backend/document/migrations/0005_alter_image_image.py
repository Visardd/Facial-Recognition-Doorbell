# Generated by Django 5.0.4 on 2024-04-27 01:22

import document.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0004_rename_image_image_image_image_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=document.models.image_upload_to),
        ),
    ]
