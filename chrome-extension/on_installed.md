# Execute code when extension is installed in Chrome.

```javascript
chrome.runtime.onInstalled.addListener(function(d) {
  if ( d.reason == "install" ) {
    console.log('installed');
  }
  else if ( d.reason == "update" ) {
    console.log('updated');
  }
});
```

- `onInstalled.addListener` - listen to installation event
- `d.reason` - contains `install` if this is a new installation or `update` if extension is installed already and just being updated
- `console.log('installed')` - execute this code when extension is freshly installed
- `console.log('updated')` - execute this code if extension is installed already and has been just updated


link_youtube: https://youtu.be/yefNFcyWM3g
