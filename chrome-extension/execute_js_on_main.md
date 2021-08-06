# Execute JavaScript on the main window

Instead of injecting code which is not the ideal solution you can execute code directly

```js
chrome.tabs.executeScript({code: "alert(1)"})
```

- `chrome.tabs.executeScript` - tell chrome to execute the script on the current tab
- `{code: "alert(1)"}` - specify the code to be executed
