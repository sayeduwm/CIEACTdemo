# Generated by Django 3.2.4 on 2021-09-16 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CIEACTapp', '0009_auto_20210913_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdatabase',
            name='TEXTVIZ',
            field=models.TextField(blank=True, null=True),
        ),
    ]
