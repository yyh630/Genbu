# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-13 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Note', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='url',
            field=models.URLField(max_length=1000, unique=True),
        ),
    ]
