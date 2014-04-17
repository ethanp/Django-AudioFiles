# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

# Enable the admin:
from django.contrib import admin
admin.autodiscover()

# [ (In a Development Mode Context:)
#   <RegexURLResolver
#       <RegexURLPattern list> (admin:admin) ^admin/>,
#   <RegexURLResolver
#       <module 'django.contrib.admindocs.urls'
#           from
#           '/Users/ethan/Library/Enthought/Canopy_64bit/User/lib/python2.7/site-packages/django/contrib/admindocs/urls.pyc'>
#       (None:None) ^admin/doc/>,
#   <RegexURLResolver
#       <module 'Conversation.v1.urls'
#           from
#           '/Users/ethan/code/non_apple/conversation/Conversation/Conversation/v1/urls.py'>
#       (None:None) ^v1/>,
#   <RegexURLPattern None ^$>,
#   <RegexURLPattern None ^media\/(?P<path>.*)$>
# ]
urlpatterns = patterns('',

    # django.conf.urls.include(module or pattern_list):
    # A function that takes a full Python import path to another
    # URLconf module that should be “included” in this place.

    # Enable admin and its documentation:
    # This isn't working right now, not sure why
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # The app itself:
    (r'^v1/', include('Conversation.v1.urls')),

    # docs.djangoproject.com/en/dev/ref/class-based-views/base/
    # RedirectView: Redirects to a given URL.
    # as_view(): Returns a callable view that takes a request and returns a response
    #            e.g. response = MyView.as_view()(request)
    (r'^$', RedirectView.as_view(url='/v1/list/')),  # <<== note trailing comma
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# this last line comes from https://docs.djangoproject.com/en/1.6/howto/static-files/
# static files include Images, Javascript, and CSS
# Note: This helper function works only in debug mode (!?)
