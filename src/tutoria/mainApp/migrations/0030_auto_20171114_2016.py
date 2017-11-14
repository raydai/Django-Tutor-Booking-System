# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-14 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0029_auto_20171113_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='balance',
            field=models.FloatField(),
        ),
    ]