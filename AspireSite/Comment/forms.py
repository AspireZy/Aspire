# -*- codinhg:utf-8 --*

__author__ = 'Aspire.Y'
__data__ = '2017/12/17 12:04'
__product__ = 'PyCharm'
__filename__ = ''


from django import forms
from .models import Comment
from django.http import HttpResponse
from django.shortcuts import render,RequestContext
from time import timezone




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        widgets = {
            forms.Textarea
        }
        fields = ['name','context',]



def remark(request):
    if request.method=='POST':
        form=CommentForm(request.POST)

        if form.is_valid():
            name=form.cleaned_data['name']
            context=form.cleaned_data['context']

            return HttpResponse(name+context)

        else:
            form=CommentForm()

        return render('test.html',{'form':form},RequestContext(request))