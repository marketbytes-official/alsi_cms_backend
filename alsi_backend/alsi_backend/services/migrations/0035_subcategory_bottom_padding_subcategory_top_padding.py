# Generated by Django 5.1.4 on 2025-01-10 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0034_specializedcategory_specializedcard'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='bottom_padding',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='top_padding',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
