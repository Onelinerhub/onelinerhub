# How to access or modify window object

Should be executed in [content script](https://developer.chrome.com/docs/extensions/mv3/content_scripts/),
which is [specified in manifest.json](/chrome-extension/content_script).

```javascript
var script = document.createElement('script');
script.textContent = 'console.log(window);';
(document.head||document.documentElement).appendChild(script);
```

- var script - init script DOM element
- script.textContent - set script content (js code)
- console.log(window); - place your window object manipulation code here
- appendChild(script) - inject script into a page
