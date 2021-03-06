# Generated by Django 3.0.4 on 2020-04-06 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carmanager', '0002_auto_20200324_2042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmanager',
            old_name='phone',
            new_name='phone1',
        ),
        migrations.AddField(
            model_name='carmanager',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='carmanager',
            name='phone2',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='carmanager',
            name='phone3',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='carmanager',
            name='position',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carmanager',
            name='telegram',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]
