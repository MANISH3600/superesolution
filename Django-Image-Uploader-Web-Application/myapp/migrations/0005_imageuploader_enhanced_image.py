# Generated by Django 3.2.22 on 2024-04-01 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20240402_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageuploader',
            name='enhanced_image',
            field=models.ImageField(blank=True, null=True, upload_to='enhanced_images'),
        ),
    ]