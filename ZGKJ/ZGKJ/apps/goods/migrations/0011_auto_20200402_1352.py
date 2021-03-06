# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-04-02 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0010_auto_20200330_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='refundorder',
            name='goodsNumber',
            field=models.CharField(default='', max_length=64, verbose_name='货号'),
        ),
        migrations.AddField(
            model_name='refundorder',
            name='goods_name',
            field=models.CharField(default='', max_length=35, verbose_name='商品名称'),
        ),
        migrations.AddField(
            model_name='refundorder',
            name='goods_spu',
            field=models.CharField(default='', max_length=70, verbose_name='商品spu编码'),
        ),
        migrations.AddField(
            model_name='refundorder',
            name='user_info',
            field=models.CharField(default='', max_length=70, verbose_name='买家信息'),
        ),
    ]
