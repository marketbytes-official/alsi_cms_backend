# Generated by Django 5.1.4 on 2024-12-20 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_industryentry_entry_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='industryentry',
            name='entry_number',
            field=models.PositiveIntegerField(),
        ),
    ]
