# How to send message from background worker to content script

```javascript
chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
  chrome.tabs.sendMessage(tabs[0].id, {some: 'value'}, function(r) {
    console.log(r)
  });
});
```

- `chrome.tabs.query` - get tabs based on specified parameters
- `active: true` - get active tabs only
- `currentWindow: true` - get currently open window
- `sendMessage` - sends message to content script on the selected tab (currently active in our case)
- `{some: 'value'}` - message to send (any object can go here)
- `console.log(r)` - callback code to process response `r` from [background message listener](/chrome-extension/listen_message_content)

group: messages


link_youtube: https://youtu.be/03ODD_wzM94
