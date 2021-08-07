# Inject Javascript into webpage from content script

Should be executed in [content script](https://developer.chrome.com/docs/extensions/mv3/content_scripts/),
which is [specified in manifest.json](/chrome-extension/content_script).

```javascript
var script = document.createElement('script');
script.textContent = 'console.log("Hi");';
(document.head||document.documentElement).appendChild(script);
```

- document.createElement - creates script DOM element
- script.textContent - script content should be placed here
- console.log("Hi"); - code we want to inject into page
- .appendChild(script) - this is where injection happens

group: inject
