# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Link, SideBar


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        super(LinkAdmin, self).save_model(request, obj, form, change)


@admin.register(SideBar)
class SideBarAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        super(SideBarAdmin, self).save_model(request, obj, form, change)
