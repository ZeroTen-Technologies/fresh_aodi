# Generated by Django 3.2 on 2022-08-24 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='fname',
        ),
    ]
