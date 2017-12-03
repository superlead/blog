# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Articles, Category, Tag


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        super(ArticlesAdmin, self).save_model(request, obj, form, change)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        super(CategoryAdmin, self).save_model(request, obj, form, change)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        super(TagAdmin, self).save_model(request, obj, form, change)