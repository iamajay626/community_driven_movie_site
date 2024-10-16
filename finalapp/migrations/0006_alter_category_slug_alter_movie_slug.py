# Generated by Django 5.0.1 on 2024-03-19 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0005_alter_movie_options_category_slug_movie_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, unique=True),
        ),
    ]
