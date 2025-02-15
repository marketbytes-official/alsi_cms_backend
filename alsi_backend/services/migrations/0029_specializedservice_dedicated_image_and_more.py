# Generated by Django 5.1.4 on 2025-01-09 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0028_specializedservice_link_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='specializedservice',
            name='dedicated_image',
            field=models.ImageField(default=1, upload_to='services/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specializedservice',
            name='dedicated_paragraph',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='specializedservice',
            name='dedicated_title',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
