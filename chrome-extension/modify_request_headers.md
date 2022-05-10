# How to modify requests headers

```javascript
chrome.webRequest.onBeforeSendHeaders.addListener( function(e) {
    for ( let header of e.requestHeaders ) {
      if ( header.name.toLowerCase() === 'user-agent' ) {
        header.value = 'some other value';
      }
    }
    return {requestHeaders: e.requestHeaders};
  }, {urls: ['<all_urls>']}, ['blocking', 'requestHeaders']
);
```

- `onBeforeSendHeaders` - let's listen to an event right before chrome is going to send requests to the server
- `e.requestHeaders` - iterate through all request headers
- `'user-agent'` - name of the header we want to modify
- `header.value` - set new value for the header we want


link_youtube: https://youtu.be/EtS560OfY_w
