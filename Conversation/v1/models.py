from django.db import models

class Recording(models.Model):
    # title = models.CharField(max_length=200)
    audioFile = models.FileField(upload_to='documents/%Y/%m/%d')
