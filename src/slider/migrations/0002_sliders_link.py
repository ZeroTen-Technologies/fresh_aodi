# Generated by Django 3.2 on 2022-09-05 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sliders',
            name='link',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
