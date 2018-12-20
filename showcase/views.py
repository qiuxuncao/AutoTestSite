# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import pymysql
import json

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


def API_MASTER(request):

    return render(request, 'showcase/API_MASTER.html')


def showcase(request):
    """
    从数据库中读取作者的用例信息，并用于前台可视化展示
    :param request:
    :return:
    """
    # 注意修改此处mysql服务的ip
    db = pymysql.connect("localhost", "root", "guchen", "guchen_test", charset='utf8')
    cursor = db.cursor()
    sql = "select * from userCaseInfo"
    cursor.execute(sql)
    results = cursor.fetchall()
    # print results
    # 向js中传递数据必须json.dumps()处理
    return render(request, "showcase/showcase.html", {'caseInfo': json.dumps(list(results))})