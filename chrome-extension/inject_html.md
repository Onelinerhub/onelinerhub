# Inject HTML into page

Should be executed in [content script](https://developer.chrome.com/docs/extensions/mv3/content_scripts/),
which is [specified in manifest.json](/chrome-extension/content_script).

```javascript
var div = document.createElement('div'); 
div.innerHTML = '<b>Hi!</b>';
document.body.appendChild(div); 
```

- var div - init div DOM element
- div.innerHTML - set HTML for new div
- document.body.appendChild(div) - inject new div (with our HTML code) into current page
