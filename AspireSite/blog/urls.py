# -*- codinhg:utf-8 --*

__author__ = 'Aspire.Y'
__data__ = '2017/12/2 23:23'
__product__ = 'PyCharm'
__filename__ = ''


from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include

from blog import views

urlpatterns = [
                  url(r'^$', views.blog, name='blog'),
                  url(r'^blog/article/(?P<article_id>\d+)$', views.ArticleAdmin, name='article_page'),
                  url(r'^blog/life/',views.Categories_Life,name='life_page'),
                  url(r'^blog/photo/',views.Categories_Photo,name='photo_page'),
                  url(r'^blog/tech/', views.Categories_Tech, name='tech_page'),
                  url(r'^blog/share/', views.Categories_Share, name='share_page'),
                  url(r'', include('Comment.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
