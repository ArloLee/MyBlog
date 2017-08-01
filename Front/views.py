# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import HttpResponse,render_to_response,render,Http404

from django.shortcuts import render

# Create your views here.

def Index_page(request):
    return render_to_response("index.html")


def Blog_page(request):
    return render_to_response("blog.html")


def About_me_page(request):
    return render_to_response("about.html")


def Subscription_page(requset):
    return render_to_response("subscription.html")

