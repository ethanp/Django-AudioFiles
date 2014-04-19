# Talk it out

## Next steps

1. `POST` a random Javascript `Blob` to the server

2. Change files listed from server to be `<audio>` tags
    * This is a change to the `templates.v1.list.html`

3. Integrate the `webaudiodemos` sample code with `POST`s to the server
    * To handle `POST`s, I need a `url` that routes to a `POST` handler method
        * This is currently happening in `views.list_saved_files(request)`
    * That handler sends (references to ?) the files to the template via `render_to_response()`


Borrows from

* [minimal-django-file-upload-example](https://github.com/axelpale/minimal-django-file-upload-example/tree/master/src/for_django_1-6/myproject/myproject/myapp)
* [Chris Wilson's WebAudioDemos](http://webaudiodemos.appspot.com/AudioRecorder/index.html)
