# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    STATUS_ITEMS = (
        (1, u'显示'),
        (2, u'隐藏'),
    )

    name = models.CharField(max_length=50, verbose_name=u'链接名称')
    href = models.URLField(verbose_name=u'链接地址')
    index = models.PositiveIntegerField(default=99, verbose_name=u'权限')
    owner = models.ForeignKey(User, verbose_name=u'创建人')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    is_display = models.CharField(default=1, choices=STATUS_ITEMS, verbose_name=u'是否显示')

    class Meta:
        verbose_name_plural = verbose_name = u'友情链接'
        ordering = ['-created_time']


class SideBar(models.Model):
    STATUS_ITEMS = (
        (1, u'显示'),
        (2, u'下线'),
    )

    SIDE_TYPE = (
        (1, u'HTML'),
        (2, u'最新文章'),
        (3, u'最热文章'),
        (4, u'最近评论'),
    )

    title = models.CharField(max_length=50, verbose_name=u'标题')
    display_type = models.PositiveIntegerField(default=1, choices=SIDE_TYPE, verbose_name=u'展示类型')
    content = models.CharField(max_length=500, blank=True, verbose_name=u'内容', help_text=u'如果设置的不是HTML类型，可为空')
    owner = models.ForeignKey(User, verbose_name=u'创建者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')

    class Meta:
        verbose_name = verbose_name_plural = u'侧边栏'