# Get active tab URL

```javascript
chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
  var tab = tabs[0];
  console.log(tab.url);
});
```

- `chrome.tabs.query` - returns tabs list based on query
- `active: true, currentWindow: true` - we want active tab
- `tab = tabs\[0\]` - we expect only one tab in the result list, which is a curent tab
- `console.log(tab.url)` - log tab URL to console

group: active_tab


link_youtube: https://youtu.be/OkyohCBKeaY
