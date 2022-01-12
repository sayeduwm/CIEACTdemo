# Generated by Django 3.2.4 on 2021-06-11 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminCrashData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OFFRNARR', models.TextField()),
                ('CRSCATGRYINT', models.IntegerField()),
                ('CRSCATGRY', models.CharField(blank=True, max_length=50, null=True)),
                ('CRSHTYPE', models.IntegerField()),
                ('INJSVR', models.CharField(blank=True, max_length=1, null=True)),
                ('CRSHDATE', models.DateField()),
                ('CRASHTIME', models.FloatField()),
                ('ONHWY', models.CharField(blank=True, max_length=50, null=True)),
                ('ONSTR', models.CharField(blank=True, max_length=50, null=True)),
                ('ATHWY', models.CharField(blank=True, max_length=50, null=True)),
                ('ATSTR', models.CharField(blank=True, max_length=50, null=True)),
                ('HWYCLASS', models.CharField(blank=True, max_length=10, null=True)),
                ('CNTYNAME', models.CharField(blank=True, max_length=50, null=True)),
                ('MUNINAME', models.CharField(blank=True, max_length=50, null=True)),
                ('MUNITYPE', models.CharField(blank=True, max_length=50, null=True)),
                ('LATDECDG', models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True)),
                ('LONDECDG', models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserCrashData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OFFRNARR', models.TextField(null=True)),
                ('CRSCATGRYINT', models.IntegerField(null=True)),
                ('CRSCATGRY', models.CharField(blank=True, max_length=50, null=True)),
                ('CRSHTYPE', models.IntegerField(null=True)),
                ('INJSVR', models.CharField(blank=True, max_length=1, null=True)),
                ('CRSHDATE', models.DateField(null=True)),
                ('CRASHTIME', models.FloatField(null=True)),
                ('ONHWY', models.CharField(blank=True, max_length=50, null=True)),
                ('ONSTR', models.CharField(blank=True, max_length=50, null=True)),
                ('ATHWY', models.CharField(blank=True, max_length=50, null=True)),
                ('ATSTR', models.CharField(blank=True, max_length=50, null=True)),
                ('HWYCLASS', models.CharField(blank=True, max_length=10, null=True)),
                ('CNTYNAME', models.CharField(blank=True, max_length=50, null=True)),
                ('MUNINAME', models.CharField(blank=True, max_length=50, null=True)),
                ('MUNITYPE', models.CharField(blank=True, max_length=50, null=True)),
                ('LATDECDG', models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True)),
                ('LONDECDG', models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=50)),
                ('EMAIL', models.EmailField(max_length=254)),
                ('DATE', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
