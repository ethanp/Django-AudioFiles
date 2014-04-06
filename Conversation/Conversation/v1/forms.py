# -*- coding: utf-8 -*-
from django import forms

class RecordingForm(forms.Form):
    audiofile = forms.FileField( label='Select a file' )
