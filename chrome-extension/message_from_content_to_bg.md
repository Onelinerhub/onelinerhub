# How to send message from content script to background script

```javascript
chrome.runtime.sendMessage({some: 'value'}, function(r) { console.log(r); });
```

- `sendMessage` - sends message to background worker
- `{some: 'value'}` - message to send (any object can go here)
- `console.log(r)` - callback code to process response `r` from [background message listener](/chrome-extension/listen_message_bg)

group: messages


link_youtube: https://youtu.be/0LOYWHBufpg
