# coding:utf-8
"""AutoTestSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from showcase import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^404/', views.notfound),
    url(r'^form_builder/', views.form_builder),
    # 入口页面为127.0.0.1:8000/base,不是index
    url(r'^basebase/', views.base),
    url(r'^layouts/', views.layouts),
    url(r'^showcase/', views.showcase),
    url(r'^ytoAutoCaseCount/', views.ytoAutoCaseCount),
    url(r'^API_MASTER/', views.API_MASTER),
    url(r'^apitest/', views.apitest),
    url(r'^addProject/',views.addProject),
    url(r'^projectList/',views.projectList),
    url(r'^bootstrapTable/',views.bootstrapTable),
]
