# Generated by Django 5.1.4 on 2024-12-19 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_differentiator_differentiatorentry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='description',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='chooses',
            name='description',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='differentiator',
            name='subtitle',
            field=models.CharField(max_length=5000),
        ),
    ]
