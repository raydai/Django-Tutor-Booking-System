# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-12 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0017_auto_20171112_1319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookedslot',
            name='duration',
        ),
        migrations.AddField(
            model_name='bookedslot',
            name='time_end',
            field=models.TimeField(default='13:00:00'),
            preserve_default=False,
        ),
    ]
