# Generated by Django 3.2.4 on 2021-08-03 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CIEACTapp', '0007_auto_20210803_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdatabase',
            name='POSBIGRAM',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='userdatabase',
            name='POSTRIGRAM',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='userdatabase',
            name='POSUNIGRAM',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]