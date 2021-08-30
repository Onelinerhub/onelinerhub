# How to close browser from background script

Should be executed in [background script](https://developer.chrome.com/docs/extensions/mv3/background_pages/),
which is [specified in manifest.json](/chrome-extension/background_script).

```javascript
chrome.tabs.query({}, function (tabs) {
  for (var i = 0; i < tabs.length; i++) {
    chrome.tabs.remove(tabs[i].id);
  }
});
```

- chrome.tabs - tabs manipulation API
- .query({} - select all tabs
- function (tabs) - define handler to execute for found tabs (all tabs in our case)
- chrome.tabs.remove - close specified tab by id
