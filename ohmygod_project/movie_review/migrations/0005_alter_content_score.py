# Generated by Django 3.2 on 2021-05-01 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_review', '0004_remove_content_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='score',
            field=models.IntegerField(default=100),
        ),
    ]
