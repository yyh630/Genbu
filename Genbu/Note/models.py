# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import datetime


# Note是基本的收藏夹单元，
class Note(models.Model):
    url = models.URLField(max_length=1000, unique=True)

    title = models.CharField(max_length=200, blank=True)

    description = models.TextField(
        verbose_name="Description",
        blank=True,
    )

    content = models.TextField(blank=True,)

    top = models.BooleanField(default=False)
    delete = models.BooleanField('delete', default=False)
    public = models.BooleanField(default=True)
    first_add_time = models.DateTimeField(auto_now_add=True)
    last_change_time = models.DateTimeField(auto_now=True)
    date = models.DateField(default=datetime.date.today)

    access_counter = models.IntegerField(default=0)
    like_counter = models.IntegerField(default=0)

    # tags = models.ManyToManyField("Tag", limit_choices_to={'hidden': False})

    def __unicode__(self):
        return self.url

    # default sorted by
    # [check] minus sign means DESC
    class Meta:
        ordering = [
            'delete',
            'date',
            '-top',
            '-last_change_time',
            'title'
        ]
