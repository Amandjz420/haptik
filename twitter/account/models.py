# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField

from .validators import phone_regex


# Create your models here.
User = get_user_model()


class People(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=True)  # validators should be a list
    birth_date = models.DateField(null=True, blank=True)
    followed = ArrayField(models.IntegerField(), blank=True, default=[])
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username
