# Console.log from background page

Should be executed in [background script](https://developer.chrome.com/docs/extensions/mv3/background_pages/),
which is [specified in manifest.json](/chrome-extension/background_script).
Also, [background debugging](https://developer.chrome.com/docs/extensions/mv3/tut_debugging/#debug_bg) should be enabled.

```javascript
console.log('test');
```

- console.log - standard console.log works fine in background scripts
- 'test' - example text to log
