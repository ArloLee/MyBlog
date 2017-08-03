# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import HttpResponse, render_to_response, render, Http404
from Front.models import Blog
from django.shortcuts import render
import json
import datetime


# Create your views here.

def Index_page(request):
    return render_to_response("index.html")


def Blog_page(request):
    Obj = Blog.objects.order_by('-id')
    print Obj
    dict = {}
    for blog in Obj:
        Id = blog.id
        Title = blog.title
        Page = blog.content
        Pub_time = blog.Pub_time
        Abs = blog.Abst
        dict[Id] = {"title": Title, "Page": Page, "Pub_time": Pub_time, "Abs": Abs}
    return render_to_response('blog.html', {"dict": dict})

def About_me_page(request):
    return render_to_response("about.html")


def Subscription_page(requset):
    return render_to_response("subscription.html")


def Article(request):
    if request.method == "GET":
        Id = request.GET["id"]
        Obj = Blog.objects.get(id=Id)
        Title = Obj.title
        Content = Obj.content
        Pub_time = Obj.Pub_time

        return render_to_response("Article.html",{"Title":Title,"Content":Content,"Pub_time":Pub_time})
