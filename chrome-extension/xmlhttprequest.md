# Make request using XMLHttpRequest

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

- `new XMLHttpRequest` - create `XMLHttpRequest` object
- `onreadystatechange` - handle request processing
- `example.org/` - send request to this URL
- `readyState == 4` - request has been executed
- `console.log(xhr.responseText)` - place your code to process response here
- `'GET'` - use GET method for request
- `xhr.send()` - send the request


link_youtube: https://youtu.be/olEr-qrnul4
