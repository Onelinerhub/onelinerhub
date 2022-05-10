# Listen for a message in content script

```javascript
chrome.runtime.onMessage.addListener(
  function(req, sender, cb) {
    console.log(req);
    cb({other: 'value'});
  }
);
```

- `onMessage.addListener` - listens to a message
- `console.log(req);` - code to process request `req` object, passed while [sending a message](/chrome-extension/mesage_from_bg_to_content)
- `cb({other: 'value'})` - send response to message sender with any object as an argument

group: messages


link_youtube: https://youtu.be/vm9hGA8Y8eA
