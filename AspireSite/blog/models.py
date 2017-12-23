#-*- coding:utf-8 -*-

from __future__ import unicode_literals
import datetime
import os
import uuid

from django.db import models
from django.utils import timezone
from django_thumbs.db.models import ImageWithThumbsField
from ckeditor.fields import RichTextField


def generate_filename(dir, filename):
    """
    安全考虑，生成随机文件名
    """
    directory_name = datetime.datetime.now().strftime('%Y/%m/%d')
    filename = uuid.uuid4().hex + os.path.splitext(filename)[-1]
    return os.path.join(directory_name, filename)



class Article(models.Model):
    _categories = {
        (u'生活随笔',u'生活随笔'),
        (u'摄像艺术',u'摄像艺术'),
        (u'技术文档',u'技术文档'),
        (u'知识分享',u'知识分享'),
    }
    categories = models.CharField(max_length=32,verbose_name='类别',choices=_categories,default='生活随笔',)
    title = models.CharField(max_length=32,verbose_name=u'标题',default='title')
    author = models.CharField(max_length=32,verbose_name=u'作者',default='Aspire.Y')
    ArticleIMGname = models.CharField (u'图片名称', max_length=100,null=True,blank=True,)
    ArticleIMG = ImageWithThumbsField(default='博客图片',verbose_name='图片', upload_to=generate_filename, sizes=((600,250),))
    context = RichTextField('文章内容')
    add_time = models.DateTimeField(verbose_name=u'添加时间',default=timezone.now)
    mod_time = models.DateTimeField(verbose_name=u'最后保存时间',auto_now=True)
    like = models.IntegerField('点赞数',default=0)

    class Meta:
        verbose_name = u'文章信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


