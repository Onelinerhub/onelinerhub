# Upload file through AJAX

```javascript
$('button').on('click', function() {
    var form = new FormData();
    form.append('file', $('input[type=file]').prop('files')[0]);
    $.ajax({
        url: '/upload', data: form, type: 'post',
        success: function(r) { console.log(r); }
     });
});
```

- 'button' - form submit button selector
- new FormData() - create [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData) object
- form.append('file' - appends ```file``` field to form data
- 'input\[type=file\]' - selector for file input with a file selected already
- /upload - path to the server-side upload script
- console.log(r) - replace with your code handling response from the server
