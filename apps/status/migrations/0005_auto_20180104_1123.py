# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-04 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0004_auto_20180104_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusinterface',
            name='portvercode',
            field=models.CharField(default='9e6f6770-f0fe-11e7-843d-201a0621d396', max_length=150, verbose_name='\u63a5\u53e3\u9a8c\u8bc1\u7801'),
        ),
    ]
