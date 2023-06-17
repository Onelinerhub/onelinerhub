# How do I download a zip file using jQuery?
// plain

Using jQuery, you can download a zip file from a server by making an AJAX request. Here is an example code block to do so:
```
$.ajax({
    url: 'http://example.com/file.zip',
    method: 'GET',
    dataType: 'binary',
    success: function(data) {
        var blob = new Blob([data], { type: 'application/zip' });
        saveAs(blob, 'file.zip');
    }
});
```
This code will make an AJAX request to the provided URL, and upon successful response, will create a Blob object with the binary data and save it as a zip file.

The code consists of the following parts:
- `$.ajax()` - makes an AJAX request to the given URL.
- `method: 'GET'` - specifies the type of request to make.
- `dataType: 'binary'` - specifies the expected data type for the response.
- `success: function(data) { ... }` - the callback to execute when the AJAX request is successful.
- `var blob = new Blob([data], { type: 'application/zip' })` - creates a Blob object with the binary data.
- `saveAs(blob, 'file.zip')` - saves the Blob object as a zip file.

## Helpful links
- [jQuery AJAX](https://api.jquery.com/jquery.ajax/)
- [HTML5 Blob](https://developer.mozilla.org/en-US/docs/Web/API/Blob)
- [FileSaver.js](https://github.com/eligrey/FileSaver.js)

onelinerhub: [How do I download a zip file using jQuery?](https://onelinerhub.com/jquery/how-do-i-download-a-zip-file-using-jquery)