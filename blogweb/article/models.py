# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Articles(models.Model):
    STATUS_ITEMS = (
        (1, u'正常'),
        (2, u'审核'),
        (3, u'删除'),
    )

    TOP_ITEMS = (
        (1, u'置顶'),
        (2, u'分类置顶'),
        (3, u'话题置顶'),
        (0, u'不置顶'),
    )
    title = models.CharField(max_length=50, verbose_name=u'标题')
    category = models.ForeignKey('Category', verbose_name=u"分类")
    cover_img = models.ImageField(max_length=30, upload_to='uploads/%Y/%m', verbose_name=u'封面图')
    tags = models.ManyToManyField('Tag', verbose_name=u'标签')
    content = models.TextField(verbose_name=u'正文')
    owner = models.ForeignKey(User, verbose_name=u'作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')
    status = models.IntegerField(default=1, choices=STATUS_ITEMS, verbose_name=u'文章状态')
    is_top = models.IntegerField(default=0, choices=TOP_ITEMS, verbose_name=u'置顶')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = verbose_name = u'文章管理'
        ordering = ['-created_time']


class Category(models.Model):
    STATUS_ITEMS = (
        (1, u'正常'),
        (2, u'审核'),
    )
    name = models.CharField(max_length=30, verbose_name=u'名称')
    cover_img = models.ImageField(max_length=30, upload_to='uploads/%Y/%m', verbose_name=u'封面图')
    title = models.CharField(max_length=50, verbose_name=u'标题')
    des = models.CharField(max_length=160, verbose_name=u'描述')
    keywords = models.CharField(max_length=100, verbose_name=u'关键词')
    owner = models.ForeignKey(User, verbose_name=u'创建人')
    status = models.IntegerField(default=1, choices=STATUS_ITEMS, verbose_name=u'栏目状态')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    is_nav = models.BooleanField(default=False, verbose_name=u'是否导航')

    def __unicode__(self):
        return self.name


    class Meta:
        verbose_name_plural = verbose_name = u'分类管理'
        ordering = ['-created_time']


class Tag(models.Model):
    STATUS_ITEMS = (
        (1, u'正常'),
        (2, u'审核'),
    )
    name = models.CharField(max_length=30, verbose_name=u'名称')
    cover_img = models.ImageField(max_length=30, upload_to='uploads/%Y/%m', verbose_name=u'封面图')
    title = models.CharField(max_length=50, verbose_name=u'标题')
    des = models.CharField(max_length=160, verbose_name=u'描述')
    keywords = models.CharField(max_length=100, verbose_name=u'关键词')
    owner = models.ForeignKey(User, verbose_name=u'创建人')
    status = models.IntegerField(default=1, choices=STATUS_ITEMS, verbose_name=u'话题状态')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    is_nav = models.BooleanField(default=False, verbose_name=u'是否导航')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = verbose_name = u'话题管理'
        ordering = ['-created_time']