# Chrome Launcher usage example

### Execute this javascript file using `nodejs`. This example will launch Chrome in headless mode and close it after 5 seconds:

```js
const chromeLauncher = require('chrome-launcher');

chromeLauncher.launch({
  port: 9222,
  chromeFlags: [ '--headless' ]
}).then(function(chrome) {
  console.log('ok');
  setTimeout(() => chrome.kill(), 1000);
});
```

- `require('chrome-launcher')` - [lib:Chrome-Launcher library](/chrome-headless/how-to-install-chrome-launcher-library) to start/stop Chrome browser programmatically
- `chromeLauncher.launch` - launch Chrome with specified params
- `port: 9222` - remote debugging protocol port
- `chrome.kill()` - close browser (or just press `Ctrl+C` in CLI)

group: cri

## Example: 
```js
nodejs test.js
```
```
ok
```

