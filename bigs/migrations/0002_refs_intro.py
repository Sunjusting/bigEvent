# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-19 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bigs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='refs',
            name='intro',
            field=models.TextField(default='hello', verbose_name='简介'),
            preserve_default=False,
        ),
    ]
