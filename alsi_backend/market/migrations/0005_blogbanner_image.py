# Generated by Django 5.1.4 on 2024-12-23 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_alter_blogentry_blog_slug_alter_blogentry_blog_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogbanner',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_banner/'),
        ),
    ]
