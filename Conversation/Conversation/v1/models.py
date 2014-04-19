# -*- coding: utf-8 -*-
from django.db import models
from datetime import date

class Recording(models.Model):
    # title = models.CharField(max_length=200)
    # user (User foreign key)
    # time (more precise than the date, which is already stored)
    # after (recursive foreign key)
    # convo (Conversation foreign key)

    # Managing Files: docs.djangoproject.com/en/1.6/topics/files/
    #
    # By default, Django stores files locally, using the MEDIA_ROOT and MEDIA_URL settings.
    #
    # When you use a FileField (or ImageField), Django provides
    # a set of APIs you can use to deal with that file.
    #
    #               TODO like what?
    #
    audiofile = models.FileField(upload_to='recordings/%Y/%m/%d')

    def __unicode__(self):
        return unicode(self.audiofile)

    def is_from_today(self):
        path_comp = self.audiofile._get_path().split('/')
        date_path = path_comp[-4:-1]  # Y/m/d
        date_comp = map(int, date_path)
        file_date = date(*date_comp)
        return file_date == date.today()

# class User(models.Model):
#     # name (CharField)
#     # password hash (???)
#     # join date (DateField)
#     # email address (EmailField)
#     # Users (aka friends) (???)
#     # Conversations (???)
#     pass
# class Conversation(models.Model):
#     # Users (aka participants)
#     # Recordings (???)
#     # first (Recording)
#     # most recent (Recording)
#     def time_of_last_activity(self): pass
#     def level_of_activity(self): pass # some sort of subjective measure
