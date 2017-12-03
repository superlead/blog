# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from blogweb.custom_admin import BaseAdmin
from .models import Articles, Category, Tag


@admin.register(Articles)
class ArticlesAdmin(BaseAdmin):
    exclude = ('owner',)


@admin.register(Category)
class CategoryAdmin(BaseAdmin):
    exclude = ('owner',)


@admin.register(Tag)
class TagAdmin(BaseAdmin):
    exclude = ('owner',)