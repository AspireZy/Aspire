# -*- codinhg:utf-8 --*

from django.conf.urls import url
from . import views
from forms import remark

app_name='Comment'

urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$',views.post_comment,name='post_comment'),
    url(r'^comment/$',remark,name='remark')
]