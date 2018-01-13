# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-13 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('content', models.TextField(blank=True)),
                ('top', models.BooleanField(default=False)),
                ('delete', models.BooleanField(default=False, verbose_name='delete')),
                ('public', models.BooleanField(default=True)),
                ('first_add_time', models.DateTimeField(auto_now_add=True)),
                ('last_change_time', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('access_counter', models.IntegerField(default=0)),
                ('like_counter', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['delete', 'date', '-top', '-last_change_time', 'title'],
            },
        ),
    ]