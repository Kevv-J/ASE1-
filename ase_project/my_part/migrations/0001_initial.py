# Generated by Django 2.1.2 on 2018-11-12 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='candidateLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_2', models.CharField(max_length=150)),
                ('candidate', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='voterLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('region', models.CharField(max_length=150)),
            ],
        ),
    ]
