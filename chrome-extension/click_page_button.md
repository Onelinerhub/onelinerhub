# How to click button on a page

Should be executed in [content script](https://developer.chrome.com/docs/extensions/mv3/content_scripts/),
which is [specified in manifest.json](/chrome-extension/content_script).

```javascript
document.querySelector('button').click();
```

- 'button' - query selector for a button to click
- .click() - triggers click event

group: trigger_event
