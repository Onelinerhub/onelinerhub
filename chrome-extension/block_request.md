# Block specific requests by URL

Should be executed in **persistent** [background script](https://developer.chrome.com/docs/extensions/mv3/background_pages/),
which is [specified in manifest.json](/chrome-extension/background_script_persistent).
Also, [webRequest](https://developer.chrome.com/docs/extensions/reference/webRequest/) permissions should be set.

```javascript
chrome.webRequest.onBeforeRequest.addListener(
  function() { return {cancel: true}; },
  { urls: ["https://example.org/page1"] },
  ["blocking"]
);
```

- onBeforeRequest.addListener - listen to request init event
- return {cancel: true} - cancel request that matched pattern
- urls - patterns to match that will trigger the listener
- "blocking" - means our listener will work in synchronous mode (we need that for blocking specific requests)
