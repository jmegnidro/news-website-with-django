# Generated by Django 3.2.20 on 2023-09-09 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20230909_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
