# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from models import Recording
from forms import RecordingForm

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = RecordingForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Recording(audiofile = request.FILES['audiofile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('Conversation.v1.views.list'))
    else:
        form = RecordingForm() # A empty, unbound form

    # Load documents for the list page
    recordings = Recording.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'v1/list.html',
        {'recordings': recordings, 'form': form},
        context_instance = RequestContext(request)
    )
