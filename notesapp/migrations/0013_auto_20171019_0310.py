# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-18 21:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0012_auto_20171018_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='created_date',
            field=models.DateField(default=datetime.date(2017, 10, 19)),
        ),
    ]
