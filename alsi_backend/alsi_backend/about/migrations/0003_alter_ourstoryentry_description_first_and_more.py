# Generated by Django 5.1.4 on 2024-12-23 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_rename_description_ourstoryentry_description_first_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourstoryentry',
            name='description_first',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ourstoryentry',
            name='description_second',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ourstoryentry',
            name='description_third',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
