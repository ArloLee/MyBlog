# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):
    content = RichTextField('正文')

    def __unicode__(self):
        return self.content