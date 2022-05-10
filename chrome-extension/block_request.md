# Block specific requests by URL

```javascript
chrome.webRequest.onBeforeRequest.addListener(
  function() { return {cancel: true}; },
  { urls: ["https://example.org/page1"] },
  ["blocking"]
);
```

- `onBeforeRequest.addListener` - listen to request init event
- `return {cancel: true}` - cancel request that matched pattern
- `urls` - patterns to match that will trigger the listener
- `"blocking"` - means our listener will work in synchronous mode (we need that for blocking specific requests)


link_youtube: https://youtu.be/T67s2mjzdNE
