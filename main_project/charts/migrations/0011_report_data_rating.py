# Generated by Django 2.1.2 on 2018-12-07 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0010_feedback_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='report_data',
            name='rating',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
