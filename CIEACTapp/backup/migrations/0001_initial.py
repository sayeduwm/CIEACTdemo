# Generated by Django 3.2.4 on 2021-08-02 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminDatabase',
            fields=[
                ('EMAIL', models.EmailField(max_length=254, null=True)),
                ('DATAID', models.CharField(blank=True, max_length=3, null=True)),
                ('CRSHNMBR', models.IntegerField(default=999, primary_key=True, serialize=False)),
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
                ('UNIPRO', models.DecimalField(decimal_places=5, max_digits=6, null=True)),
                ('BIPRO', models.DecimalField(decimal_places=5, max_digits=6, null=True)),
                ('TRIPRO', models.DecimalField(decimal_places=5, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DistractedBigram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bigrams', models.CharField(blank=True, max_length=30, null=True)),
                ('Probability', models.DecimalField(blank=True, decimal_places=5, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DistractedTrigram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Trigram', models.CharField(blank=True, max_length=60, null=True)),
                ('Probability', models.DecimalField(blank=True, decimal_places=5, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DistractedUnigram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unigrams', models.CharField(blank=True, max_length=30, null=True)),
                ('Probability', models.DecimalField(blank=True, decimal_places=5, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InattentivedBigram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bigrams', models.CharField(blank=True, max_length=30, null=True)),
                ('Probability', models.DecimalField(blank=True, decimal_places=5, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InattentiveTrigram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Trigram', models.CharField(blank=True, max_length=60, null=True)),
                ('Probability', models.DecimalField(blank=True, decimal_places=5, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InattentiveUnigram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unigrams', models.CharField(blank=True, max_length=30, null=True)),
                ('Probability', models.DecimalField(blank=True, decimal_places=5, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserDatabase',
            fields=[
                ('EMAIL', models.EmailField(max_length=254, null=True)),
                ('DATAID', models.CharField(blank=True, max_length=3, null=True)),
                ('CRSHNMBR', models.IntegerField(default=999, primary_key=True, serialize=False)),
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
                ('UNIPRO', models.DecimalField(decimal_places=5, max_digits=6, null=True)),
                ('BIPRO', models.DecimalField(decimal_places=5, max_digits=6, null=True)),
                ('TRIPRO', models.DecimalField(decimal_places=5, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfoDatabase',
            fields=[
                ('NAME', models.CharField(max_length=50)),
                ('EMAIL', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('DATE', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MODELNAME', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WorkzoneBigram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bigrams', models.CharField(blank=True, max_length=30, null=True)),
                ('Probability', models.DecimalField(blank=True, decimal_places=5, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkzoneTrigram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Trigram', models.CharField(blank=True, max_length=60, null=True)),
                ('Probability', models.DecimalField(blank=True, decimal_places=5, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkzoneUnigram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unigrams', models.CharField(blank=True, max_length=30, null=True)),
                ('Probability', models.DecimalField(blank=True, decimal_places=5, max_digits=6, null=True)),
            ],
        ),
    ]
