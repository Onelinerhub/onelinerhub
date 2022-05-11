# Get object from chrome.storage

```javascript
chrome.storage.sync.get(['obj'], function(res) { console.log(res.obj); });
```

- `chrome.storage` - extension storage API
- `.get` - gets objects from storage by specified keys
- `\['obj'\]` - array of keys to get from storage (we only ask for one `obj` key)
- `console.log(res.obj)` - code to manipulate object from storage (saved to `obj` key)

group: storage


link_youtube: https://youtu.be/nC1nwpk3kIQ
