# Generated by Django 4.2.9 on 2024-01-19 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
        migrations.AddField(
            model_name='post',
            name='ccategories',
            field=models.ManyToManyField(to='news.category'),
        ),
    ]
