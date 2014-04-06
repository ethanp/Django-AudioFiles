# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('Conversation.v1.views',
    url(r'^list/$', 'list', name='list'),
)
