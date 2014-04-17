# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('Conversation.v1.views',

    # if this method is sent a POST request with the contents
    # of a file to save, it saves it.
    url(r'^list/$', 'list_saved_files', name='list'),
)
