# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name="标题")
    content = RichTextField(blank=True, null=True, verbose_name="内容")
    Publish_time = models.CharField(blank=False, null=False, verbose_name="发布时间",max_length=16)
    Pub_time = models.DateTimeField(blank=False, null=False, verbose_name="发布时间")
    Abst = models.TextField(blank=False, null=False, verbose_name="摘要", max_length=256)
    def __unicode__(self):
        return self.title