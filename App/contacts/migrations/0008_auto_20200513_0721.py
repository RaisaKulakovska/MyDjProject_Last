# Generated by Django 3.0.4 on 2020-05-13 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_remove_contacts_surname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacts',
            old_name='description',
            new_name='testimonial',
        ),
    ]
