# -*- coding: utf-8 -*-
from django.db import models

class Recording(models.Model):
    # title = models.CharField(max_length=200)
    audiofile = models.FileField(upload_to='recordings/%Y/%m/%d')
