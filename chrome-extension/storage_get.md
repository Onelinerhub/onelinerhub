# Get object from chrome.storage

Should be executed in [content script](https://developer.chrome.com/docs/extensions/mv3/content_scripts/),
which is [specified in manifest.json](/chrome-extension/storage).

```javascript
chrome.storage.sync.get(['obj'], function(res) { console.log(res.obj); });
```

- chrome.storage - extension storage API
- .get - gets objects from storage by specified keys
- \['obj'\] - array of keys to get from storage (we only ask for one `obj` key)
- console.log(res.obj) - code to manipulate object from storage (saved to `obj` key)

group: storage
