# Generated by Django 4.1.6 on 2023-03-06 06:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_fullfillment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fullfillment_Date',
            field=models.DateField(default=datetime.datetime(2023, 3, 13, 11, 32, 37, 100726)),
        ),
    ]
