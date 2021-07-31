# Listen for a message in content script

Should be executed in [content script](https://developer.chrome.com/docs/extensions/mv3/content_scripts/),
which is [specified in manifest.json](/chrome-extension/content_script).

```javascript
chrome.runtime.onMessage.addListener(
  function(req, sender, cb) {
    console.log(req);
    cb({other: 'value'});
  }
);
```

- onMessage.addListener - listens to a message
- console.log(req); - code to process request `req` object, passed while [sending a message](/chrome-extension/mesage_from_bg_to_content)
- cb({other: 'value'}) - send response to message sender with any object as an argument

group: messages
