# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-13 03:51
from __future__ import unicode_literals

import bigs.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_auto_20170105_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bigs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=160, verbose_name='事件')),
                ('year', models.CharField(max_length=50, verbose_name='年代')),
                ('date', models.CharField(max_length=50, verbose_name='时间')),
                ('era', models.CharField(max_length=80, verbose_name='朝代')),
                ('place', models.CharField(max_length=80, verbose_name='地点')),
                ('roles', models.CharField(max_length=254, verbose_name='人物')),
                ('content', models.TextField(verbose_name='详情')),
                ('memo', models.TextField(verbose_name='备注')),
                ('comments', models.TextField(verbose_name='点评')),
                ('image', models.ImageField(upload_to=bigs.models.get_file_path, verbose_name='事件图片')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('status', models.SmallIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Refs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('author', models.CharField(max_length=100, verbose_name='作者')),
                ('publisher', models.CharField(max_length=100, verbose_name='出版社')),
                ('pubtime', models.DateTimeField(verbose_name='出版时间')),
                ('cover', models.ImageField(upload_to=bigs.models.get_file_path, verbose_name='封面')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.SmallIntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='bigs',
            name='refs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bigs.Refs'),
        ),
        migrations.AddField(
            model_name='bigs',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.User'),
        ),
    ]
