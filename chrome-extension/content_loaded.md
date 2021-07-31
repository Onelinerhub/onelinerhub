# How to execute content script after page content is loaded

Should be executed in [content script](https://developer.chrome.com/docs/extensions/mv3/content_scripts/),
which is [specified in manifest.json](/chrome-extension/content_script).

```javascript
document.addEventListener('DOMContentLoaded', function() {
  console.log('loaded');
});
```

- document.addEventListener - listen for a document event
- DOMContentLoaded - event triggers when page is fully loaded
- console.log('loaded') - place your code here to execute after page load is complete
