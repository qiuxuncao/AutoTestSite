# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, 'showcase/index.html')


def notfound(request):

    return render(request, 'showcase/404.html')


def form_builder(request):

    return render(request, 'showcase/form_builder.html')


def base(request):

    return render(request, 'showcase/base.html')


def layouts(request):

    return render(request, 'showcase/layouts.html')