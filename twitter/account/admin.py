# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
# -*- coding: utf-8 -*-

from .models import People


class PeopleAdmin(admin.ModelAdmin):
    """
    Admin for PeopleAdmin
    """

    list_display = [f.name for f in People._meta.fields]


admin.site.register(People, PeopleAdmin)