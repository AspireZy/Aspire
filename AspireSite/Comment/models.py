#-*- coding:utf-8 -*-

from __future__ import unicode_literals



from django.db import models

# Create your models here.


import datetime
import os
import uuid

from django.db import models
from django.utils import timezone
from django_thumbs.db.models import ImageWithThumbsField






class Comment(models.Model):
    name = models.CharField('名字',max_length=32,)
    context = models.TextField('评论内容', max_length= 280,)
    created_time = models.DateTimeField('添加时间',default=timezone.now,)
    post = models.ForeignKey('blog.Article')


    class Meta:
        verbose_name = u'评论信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.context[:20]



