# Generated by Django 5.1.4 on 2024-12-12 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='banner/')),
                ('decription', models.TextField()),
                ('link_name', models.CharField(max_length=255)),
                ('link_url', models.URLField()),
            ],
        ),
    ]
