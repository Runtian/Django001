# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 14:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accountant', '0006_auto_20170604_0715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productorder',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='productpurchase',
            name='discount',
        ),
    ]
