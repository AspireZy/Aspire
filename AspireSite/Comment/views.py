# -*- codinhg:utf-8 --*

# Create your views here.

from django.shortcuts import render,get_object_or_404,redirect

from blog.models import Article
from .forms import CommentForm
from django.template import RequestContext

from django.views.decorators.csrf import csrf_protect
# Create your views here.


@csrf_protect
def post_comment(request,post_pk):
    post = get_object_or_404(Article,pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            comment = form.save(commit=False)
            print(1)

            comment.post = post

            comment.save()

            return redirect(post)


        else:
            comment_list = post.comment_set.all()

            context = {
                'post':post,
                'form':form,
                'comment_list':comment_list
            }

            return render(request,'test.html',context_instance=RequestContext(request))

    return render(post)