# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-17 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_auto_20200117_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='reason',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='取消订单原因'),
        ),
    ]
