# Generated by Django 5.1.4 on 2024-12-26 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_rename_banner_img_gallery_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleryimage',
            name='caption',
        ),
    ]
