# Generated by Django 3.2 on 2022-09-13 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blogcomment_comment_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='reply',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
