# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-30 15:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180830_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='history',
        ),
    ]
