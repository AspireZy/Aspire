# -*- codinhg:utf-8 --*

__author__ = 'Aspire.Y'
__data__ = '2017/12/2 23:27'
__product__ = 'PyCharm'
__filename__ = ''

import xadmin

# Register your models here.

from .models import Article
from Comment.models import *



class ArticleAdmin(object):
    list_display = ('title','add_time','mod_time','ArticleIMGname','like')

class CommentAdmin(object):
    list_display = ('name','context','created_time')




xadmin.site.register(Article,ArticleAdmin)

xadmin.site.register(Comment,CommentAdmin)

