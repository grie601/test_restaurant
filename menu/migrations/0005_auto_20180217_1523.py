# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-02-17 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20180217_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishes',
            name='image',
            field=models.ImageField(upload_to='/images/', verbose_name='Изображение'),
        ),
    ]
