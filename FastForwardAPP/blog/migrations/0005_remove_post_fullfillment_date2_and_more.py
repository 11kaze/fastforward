# Generated by Django 4.1.6 on 2023-03-06 09:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_fullfillment_date2_alter_post_fullfillment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='fullfillment_Date2',
        ),
        migrations.AlterField(
            model_name='post',
            name='fullfillment_Date',
            field=models.DateField(default=datetime.datetime(2023, 3, 13, 15, 29, 40, 504257)),
        ),
    ]
