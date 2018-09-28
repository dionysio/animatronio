#!/usr/bin/env python
#-*- coding: utf-8 -*-

from django.conf.urls import url


from . import views

urlpatterns = [url(r'hello/$', views.Contact.as_view(), name='contact'),
                url(r'^$', views.HomeView.as_view(), name='index'),
            ]
