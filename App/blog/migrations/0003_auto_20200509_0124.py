# Generated by Django 3.0.4 on 2020-05-08 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
        migrations.AddField(
            model_name='blog',
            name='author_id',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='car_id',
            field=models.IntegerField(default=True),
        ),
    ]
