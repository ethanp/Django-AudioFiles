# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import Recording
from forms import RecordingForm

def list_saved_files(request):
    # Handle file upload
    if request.method == 'POST':

        # https://docs.djangoproject.com/en/dev/ref/request-response
        #
        # request.POST: A dictionary-like object containing all given
        # HTTP POST parameters, providing that the request contains form data.
        # Note: POST does *not* include file-upload information.
        #
        # request.FILES: A dictionary-like object containing all uploaded files.
        # Each key in FILES is the name from the <input type="file" name="" />.
        # Each value in FILES is an UploadedFile.
        # Note: This only has data if the <form> that POSTed had enctype="multipart/form-data"
        form = RecordingForm(request.POST, request.FILES)
        if form.is_valid():
            newrec = Recording(audiofile=request.FILES['audiofile'])
            newrec.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('Conversation.v1.views.list'))
    else:
        form = RecordingForm()  # An empty, unbound form

    # Load documents for the list page
    recordings = Recording.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'v1/list.html',
        {'recordings': recordings, 'form': form},
        context_instance=RequestContext(request)
    )

def recorder_screen(request):
    if request.method == 'POST':
        newrec = Recording(audiofile=request.FILES['recording'])
        newrec.save()
        return HttpResponseRedirect(reverse('Conversation.v1.views.recorder_screen'))
    else:
        form = RecordingForm()

    return render_to_response(
        'v1/Audio Recorder.html',
        {'form' : form},
        context_instance=RequestContext(request)
    )
