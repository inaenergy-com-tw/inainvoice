# Generated by Django 3.1.5 on 2021-01-29 08:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0012_Fix_decimal_prec'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='filldate',
            field=models.DateField(default=datetime.datetime(2021, 1, 29, 8, 41, 3, 573514, tzinfo=utc)),
        ),
    ]
