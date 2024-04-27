# Generated by Django 5.0.4 on 2024-04-26 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0003_image_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='Image',
            new_name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.CharField(default='default', max_length=50),
        ),
    ]
