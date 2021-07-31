# Make request using XMLHttpRequest

Should be executed in [content script](https://developer.chrome.com/docs/extensions/mv3/content_scripts/),
which is [specified in manifest.json](/chrome-extension/content_script).
Make sure to set [host permissions](/chrome-extension/host_permissions) you want to access.

```javascript
var xhr = new XMLHttpRequest();
xhr.onreadystatechange = function(r) {
  if ( xhr.readyState == 4 ) {
    console.log(xhr.responseText);
  }
});
xhr.open('GET', 'https://example.org/');
xhr.send();
```

- new XMLHttpRequest - create `XMLHttpRequest` object
- onreadystatechange - handle request processing
- example.org/ - send request to this URL
- readyState == 4 - request has been executed
- console.log(xhr.responseText) - place your code to process response here
- 'GET' - use GET method for request
- xhr.send() - send the request
