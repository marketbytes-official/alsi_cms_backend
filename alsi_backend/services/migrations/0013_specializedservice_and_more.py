# Generated by Django 5.1.4 on 2024-12-31 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0012_alter_subservicescategoryentry_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecializedService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=2000)),
                ('image', models.ImageField(upload_to='services/')),
            ],
        ),
        migrations.AlterField(
            model_name='subservicescategoryentry',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='services/'),
        ),
    ]
