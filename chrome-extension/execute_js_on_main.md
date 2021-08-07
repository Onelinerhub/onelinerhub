# Inject javascript into webpage from the background script

Should be executed in [background script](https://developer.chrome.com/docs/extensions/mv3/background_pages/).

```js
chrome.tabs.executeScript({code: "alert(1)"})
```

- chrome.tabs.executeScript - tell chrome to execute the script on the current tab
- alert(1) - code to be executed

group: inject
