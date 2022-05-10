# How to close browser from background script

```javascript
chrome.tabs.query({}, function (tabs) {
  for (var i = 0; i < tabs.length; i++) {
    chrome.tabs.remove(tabs[i].id);
  }
});
```

- `chrome.tabs` - tabs manipulation API
- `.query({}` - select all tabs
- `function (tabs)` - define handler to execute for found tabs (all tabs in our case)
- `chrome.tabs.remove` - close specified tab by id


link_youtube: https://youtu.be/XFqRTNaa-Kk
