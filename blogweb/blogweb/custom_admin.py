# -*- encoding:utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(BaseAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        super(BaseAdmin, self).save_model(request, obj, form, change)