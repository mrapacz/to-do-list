# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0004_auto_20160606_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='date',
            field=models.DateField(unique=True, verbose_name=b"day's happening time"),
        ),
    ]
