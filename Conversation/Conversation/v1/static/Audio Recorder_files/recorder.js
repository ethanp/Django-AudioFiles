/*License (MIT)

 Copyright © 2013 Matt Diamond

 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
 documentation files (the "Software"), to deal in the Software without restriction, including without limitation
 the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and
 to permit persons to whom the Software is furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all copies or substantial portions of
 the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
 THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
 CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
 DEALINGS IN THE SOFTWARE.

 Modified 4/6/2014 Ethan Petuchowski
 */

(function (window) {

    // this is a background task that can be executed asynchronously,
    // I believe there is no other way to do multithreading in Javascript
    // the file doesn't exist though
    var WORKER_PATH = '/static/Audio%20Recorder_files/recorderWorker.js';

    // "source" is the "inputPoint", i.e. the GainNode
    // We're not passing in a "cfg"
    var Recorder = function (source, cfg) {
        var config = cfg || {};
        var bufferLen = config.bufferLen || 4096;

        // Retrieve the AudioContext graph object
        this.context = source.context;

        // Check if the AudioContext has the method "createScriptProcessor".
        // It renamed the old "createJavaScriptNode" method, but we must make
        // sure the new version it exists first.
        if (!this.context.createScriptProcessor) {
            this.node = this.context.createJavaScriptNode(bufferLen, 2, 2);
        } else {

            // Receives (buffersize, # input channels, # output channels).
            // Creates a "ScriptProcessorNode", an audio-processing module
            // whose "onaudioprocess" function gets called whenever the
            // "buffersize" frames have been filled (~20 times per second).
            this.node = this.context.createScriptProcessor(bufferLen, 2, 2);
        }

        // I'm not sure where this is coming from. The WORKER_PATH doesn't exist
        // in this directory, and the config is an empty object in this case.
        var worker = new Worker(config.workerPath || WORKER_PATH);

        // Initialize the worker by setting its sampleRate attribute
        worker.postMessage({
            command: 'init',
            config: {
                sampleRate: this.context.sampleRate
            }
        });
        var recording = false,
            currCallback;

        // Called whenever the audio data buffer fills up
        this.node.onaudioprocess = function (e) {
            if (!recording) return;

            // The Worker has L & R arrays building up the entire audio file
            // We're just passing new buffers to be appended to them
            worker.postMessage({
                command: 'record',
                buffer: [

                    // Retrieve Float32Array of audio data for channels 0 and 1 (stereo)
                    e.inputBuffer.getChannelData(0),
                    e.inputBuffer.getChannelData(1)
                ]
            });
        };

        this.configure = function (cfg) {
            for (var prop in cfg) {
                if (cfg.hasOwnProperty(prop)) {
                    config[prop] = cfg[prop];
                }
            }
        };

        this.record = function () {
            recording = true;
        };

        this.stop = function () {
            recording = false;
        };

        this.clear = function () {
            worker.postMessage({ command: 'clear' });
        };

        this.getBuffers = function (cb) {
            currCallback = cb || config.callback;
            worker.postMessage({ command: 'getBuffer' })
        };

        this.exportWAV = function (cb, type) {
            // This callback sets up the HDD button to download the file
            currCallback = cb || config.callback;
            type = type || config.type || 'audio/wav'; // we're using the default
            if (!currCallback) throw new Error('Callback not set');
            worker.postMessage({
                command: 'exportWAV',
                type: type
            });
        };

        this.exportMonoWAV = function (cb, type) {
            currCallback = cb || config.callback;
            type = type || config.type || 'audio/wav';
            if (!currCallback) throw new Error('Callback not set');
            worker.postMessage({
                command: 'exportMonoWAV',
                type: type
            });
        };

        //
        worker.onmessage = function (e) {
            var blob = e.data;
            currCallback(blob);
        };

        source.connect(this.node);
        // if the script node is not connected to an output
        // the "onaudioprocess" event is not triggered in chrome.
        this.node.connect(this.context.destination);
    };

    /**
     * Set the HDD button in the interface to be "activated" such that
     * when a user clicks it, their browser prompts them to download
     * the @blob of data with default @filename. This @blob happens
     * to be the audio file.
     */
    // TODO something analogous (i.e. another <a> tag) that POSTs the blob to the server with AJAX
    Recorder.setupDownload = function (blob, filename) {

        // create a resource locator for the data
        // will be something like: blob:d3958f5c-0777-0845-9dcf-2cb28783acaf
        var blob_url = (window.URL || window.webkitURL).createObjectURL(blob);

        // this is an <a> tag with the HDD image on top
        var link = document.getElementById("save");

        // set it to be a link to the data
        link.href = blob_url;

        // * This attribute signifies that the resource it points to should be
        //   downloaded by the browser rather than navigated to.
        // * The value specifies the default filename that the author recommends
        //   for use in labeling the resource in a local file system.
        link.download = filename || 'output.wav';

        this.post_from_form('/v1/upload/', filename, {
            blob_url : blob_url,
            type   : 'wav'
        });
    };

    // TODO this should be moved to main.js or something
    Recorder.post_from_form = function (path, filename, inputs) {
        var form = document.getElementById("recording-file-form");
        var input = document.createElement("input");
        input.setAttribute("type", "hidden");
        input.setAttribute("name", "something_or_other");
        input.setAttribute("value", 'abc');  //JSON.stringify(inputs));
        form.appendChild(input);
        form.submit();
    };

    window.Recorder = Recorder;

})(window);
