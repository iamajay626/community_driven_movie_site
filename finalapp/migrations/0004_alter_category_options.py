# Generated by Django 5.0.1 on 2024-03-18 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0003_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]