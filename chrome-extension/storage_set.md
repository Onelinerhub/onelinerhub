# Save object to chrome.storage

```javascript
chrome.storage.sync.set({obj: 'Hi'}, function() { console.log('saved'); });
```

- `chrome.storage` - extension storage API
- `.set` - saves object to storage by specified key
- `obj` - key to save our object under
- `'Hi'` - example object to save (simple string in our case)
- `console.log('saved')` - because `set` is asynchronous, we specify callback to know when object is actually saved

group: storage


link_youtube: https://youtu.be/BW0_GHxmvLE
