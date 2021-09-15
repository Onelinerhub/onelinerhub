# Open new tab

Should be executed in [background script](https://developer.chrome.com/docs/extensions/mv3/background_pages/).
[Tabs permissions](https://developer.chrome.com/docs/extensions/reference/tabs/#manifest) should be set in `manifest.json`.

```javascript
chrome.tabs.create({ url: "https://example.org/" });
```

- browserAction.onClicked - example listener, listen to extension icon click in our case
- chrome.tabs.create - open new tab
- url: - URL of a new tab
