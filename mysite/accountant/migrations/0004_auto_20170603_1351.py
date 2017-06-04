# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 13:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountant', '0003_auto_20170602_0827'),
    ]

    operations = [
        migrations.AddField(
            model_name='productorder',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='\u751f\u4ea7\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='productorder',
            name='discount',
            field=models.FloatField(verbose_name='\u4f18\u60e0'),
        ),
    ]