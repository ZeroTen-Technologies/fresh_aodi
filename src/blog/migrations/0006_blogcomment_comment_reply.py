# Generated by Django 3.2 on 2022-09-13 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogcomment_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='comment_reply',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
