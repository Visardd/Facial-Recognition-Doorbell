# Generated by Django 5.0.4 on 2024-04-26 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]