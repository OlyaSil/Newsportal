# Generated by Django 4.2.9 on 2024-01-21 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_remove_post_categories_post_ccategories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='ccategories',
            new_name='categories',
        ),
    ]
