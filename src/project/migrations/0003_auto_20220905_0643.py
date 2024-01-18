# Generated by Django 3.2 on 2022-09-05 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_projectcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='amount',
            field=models.IntegerField(blank=True, default=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='currency',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]