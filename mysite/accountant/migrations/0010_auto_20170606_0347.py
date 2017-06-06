# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 03:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accountant', '0009_auto_20170606_0142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, verbose_name='\u6458\u8981')),
                ('amount', models.FloatField(verbose_name='\u91d1\u989d')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='\u65e5\u671f')),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, verbose_name='\u6458\u8981')),
                ('amount', models.FloatField(verbose_name='\u91d1\u989d')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='\u65e5\u671f')),
            ],
        ),
        migrations.CreateModel(
            name='Payee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='\u6536\u6b3e\u4eba')),
            ],
        ),
        migrations.CreateModel(
            name='Payer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='\u4ed8\u6b3e\u4eba')),
            ],
        ),
        migrations.AddField(
            model_name='income',
            name='payer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accountant.Payer', verbose_name='\u4ed8\u6b3e\u4eba'),
        ),
        migrations.AddField(
            model_name='expense',
            name='Payee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accountant.Payer', verbose_name='\u6536\u6b3e\u4eba/\u7528\u9014'),
        ),
    ]
