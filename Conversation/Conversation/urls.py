# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

# Enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Enable admin and its documentation:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # The app itself:
    (r'^v1/', include('Conversation.v1.urls')),
    (r'^$', RedirectView.as_view(url='/v1/list/')), # <<== note trailing comma
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
