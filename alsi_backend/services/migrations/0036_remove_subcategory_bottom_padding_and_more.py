# Generated by Django 5.1.4 on 2025-01-12 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0035_subcategory_bottom_padding_subcategory_top_padding'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='bottom_padding',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='top_padding',
        ),
    ]
