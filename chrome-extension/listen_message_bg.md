# Listen for a message in background script

Should be executed in [background script](https://developer.chrome.com/docs/extensions/mv3/background_pages/),
which is [specified in manifest.json](/chrome-extension/background_script).

```javascript
chrome.runtime.onMessage.addListener(
  function(req, sender, cb) {
    console.log(req);
    cb({other: 'value'});
  }
);
```

- onMessage.addListener - listens to a message
- console.log(req); - code to process request `req` object, passed while [sending a message](/chrome-extension/message_from_content_to_bg)
- cb({other: 'value'}) - send response to message sender with any object as an argument

group: messages
