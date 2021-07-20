# How to access page variables

Should be executed in [content script](https://developer.chrome.com/docs/extensions/mv3/content_scripts/),
which is [specified in manifest.json](/chrome-extension/content_script).

```javascript
var script = document.createElement('script');
script.textContent = 'console.log(page_var);';
(document.head||document.documentElement).appendChild(script);
```

- var script - init script DOM element
- script.textContent - set script content (js code)
- console.log(page_var); - sample code to access page variable (`page_var` is a variable defined within loaded page)
- appendChild(script) - inject script into a page
