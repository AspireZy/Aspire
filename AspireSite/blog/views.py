# Create your views here.
# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from . import models
from blog.models import Article
from django.http import HttpResponse

from Comment.forms import CommentForm
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt



def index(request):
    return render (request, "index.html")

ONE_PAGE_OF_DATA = 3

def blog(rq):
    try:
        curPage = int (rq.GET.get('curPage', '1'))
        allPage = int (rq.GET.get('allPage', '1'))
        pageType = str (rq.GET.get('pageType', ''))

    except ValueError:
        curPage = 1
        allPage = 1
        pageType = ''

    if pageType == 'pageDown':
        curPage += 1

    elif pageType == 'pageUp':
        curPage -= 1

    startPos = (curPage - 1) * ONE_PAGE_OF_DATA
    endPos = startPos + ONE_PAGE_OF_DATA
    posts = Article.objects.all()[startPos:endPos]


    if curPage == 1 and allPage == 1:
        allPostCounts = Article.objects.count()
        allPage = allPostCounts / ONE_PAGE_OF_DATA
        remainPost = allPostCounts % ONE_PAGE_OF_DATA

        if remainPost > 0:
            allPage += 1

    return render_to_response('blog.html', {'posts': posts,'allPage': allPage,'curPage':curPage},context_instance=RequestContext(rq))



@csrf_protect
@csrf_exempt
def ArticleAdmin(request, article_id):

    posts = models.Article.objects.get(pk = article_id)

    form = CommentForm()
    comment_list = posts.comment_set.all()
    comment_count = posts.comment_set.all().count


    if request.method == 'POST':
        form = CommentForm(request.POST)

        if request.POST.get('Data'):
            posts.like += 1
            posts.save()

        if form.is_valid():


            comment = form.save(commit=False)

            comment.post = posts

            comment.save()


        else:
            pass





    context = {
        'posts':posts,
        'form':form,
        'comment_list':comment_list,
        'comment_count':comment_count,
    }





    return render(request,"test.html",context=context)


def Categories_Life(request):
    try:
        life_posts = models.Article.objects.filter(categories='生活随笔').order_by('-id')

    except Article.DoesNotExist:
        pass

    return render(request, 'category_life.html', {"life_posts": life_posts, })

def Categories_Photo(request):
    try:
        photo_posts = models.Article.objects.filter(categories='摄像艺术').order_by('-id')

    except Article.DoesNotExist:
        pass

    return render(request, 'category_photo.html', {"photo_posts": photo_posts, })

def Categories_Tech(request):
    try:
        tech_posts = models.Article.objects.filter(categories='技术文档').order_by('-id')
    except Article.DoesNotExist:
        pass

    return render(request, 'category_tech.html', {"tech_posts": tech_posts, })

def Categories_Share(request):
    try:
        share_posts = models.Article.objects.filter(categories='知识分享').order_by('-id')
    except Article.DoesNotExist:
        pass

    return render(request, 'category_share.html', {'share_posts':share_posts, })









