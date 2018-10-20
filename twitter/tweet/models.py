# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from account.models import People


class Tweet(models.Model):

    title = models.CharField(max_length=30)  # validators should be a list
    msg = models.CharField(max_length=140)
    like = models.IntegerField(default=0)
    people = models.ForeignKey(People, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
