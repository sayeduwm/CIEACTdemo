# Generated by Django 3.2.4 on 2021-08-03 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CIEACTapp', '0002_rename_inattentivedbigram_inattentivebigram'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdatabase',
            name='BIPRO',
        ),
        migrations.RemoveField(
            model_name='userdatabase',
            name='TRIPRO',
        ),
        migrations.RemoveField(
            model_name='userdatabase',
            name='UNIPRO',
        ),
        migrations.AddField(
            model_name='userdatabase',
            name='NOISYORB',
            field=models.DecimalField(decimal_places=5, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='userdatabase',
            name='NOISYORT',
            field=models.DecimalField(decimal_places=5, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='userdatabase',
            name='NOISYORU',
            field=models.DecimalField(decimal_places=5, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='userdatabase',
            name='NOISYORUB',
            field=models.DecimalField(decimal_places=5, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='userdatabase',
            name='POSBIGRAM',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userdatabase',
            name='POSTRIGRAM',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userdatabase',
            name='POSUNIGRAM',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]