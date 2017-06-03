"""mysite_talkapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from talkapp import views


urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^users/create/$', views.user_create, name='user_create'),
    url(r'^users/store/$', views.user_store, name='user_store'),
    url(r'^users/edit/$', views.user_edit, name='user_edit'),
    url(r'^users/update/$', views.user_update, name='user_update'),

    url(r'^posts/$', views.post_index, name='post_index'),
    url(r'^posts/create/$', views.post_create, name='post_create'),
    url(r'^posts/store/$', views.post_store, name='post_store'),
    url(r'^posts/(?P<id>\d+)/$', views.post_show, name='post_show'),
    url(r'^posts/(?P<id>\d+)/destroy$', views.post_destroy, name='post_destroy'),

    url(r'^posts/(?P<post_id>\d+)/comments/create/$', views.comment_create, name='comment_create'),
    url(r'^posts/(?P<post_id>\d+)/comments/store/$', views.comment_store, name='comment_store'),

    url(r'^getlogin/$', views.getLogin, name='getlogin'),
    url(r'^postlogin/$', views.postLogin, name='postlogin'),
    url(r'^getlogout/$', views.getLogout, name='getlogout'),]
