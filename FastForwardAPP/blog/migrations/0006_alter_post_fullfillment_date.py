# Generated by Django 4.1.6 on 2023-03-07 13:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_fullfillment_date2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fullfillment_Date',
            field=models.DateField(default=datetime.datetime(2023, 3, 14, 19, 23, 1, 590405)),
        ),
    ]
