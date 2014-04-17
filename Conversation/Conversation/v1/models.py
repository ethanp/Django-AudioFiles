# -*- coding: utf-8 -*-
from django.db import models
from datetime import date

class Recording(models.Model):
    # title = models.CharField(max_length=200)

    # Managing Files: docs.djangoproject.com/en/1.6/topics/files/
    #
    # By default, Django stores files locally, using the MEDIA_ROOT and MEDIA_URL settings.
    #
    # When you use a FileField (or ImageField), Django provides
    # a set of APIs you can use to deal with that file.
    audiofile = models.FileField(upload_to='recordings/%Y/%m/%d')

    def __unicode__(self):
        return unicode(self.audiofile)

    def is_from_today(self):
        path_components = self.audiofile._get_path().split('/')
        date_path = path_components[-4:-1]
        date_components = map(int, date_path)
        file_date = date(*date_components)
        return file_date == date.today()
