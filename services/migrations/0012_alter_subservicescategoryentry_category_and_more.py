# Generated by Django 5.1.4 on 2024-12-31 05:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_alter_subservicescategory_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subservicescategoryentry',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.subservicescategory'),
        ),
        migrations.AlterField(
            model_name='subservicescategoryentry',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='subservicescategoryentry',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
