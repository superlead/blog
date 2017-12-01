# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from article.models import Articles


class Comment(models.Model):
    article = models.ForeignKey(Articles, verbose_name=u'文章')
    author = models.CharField(max_length=10, verbose_name=u'昵称')
    email = models.EmailField(verbose_name=u'邮箱')
    content = models.TextField(verbose_name=u'评论', default=True, help_text=u'请文明留言,遵守相关法律法规!')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')
    status = models.BooleanField(default=False, verbose_name=u'是否显示')

    class Meta:
        verbose_name_plural = verbose_name = u'评论管理'