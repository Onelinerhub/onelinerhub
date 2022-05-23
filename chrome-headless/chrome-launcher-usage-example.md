# Chrome Launcher usage example

### This example will launch Chrome in headless mode and close it after 5 seconds

```js
const chromeLauncher = require('chrome-launcher');

chromeLauncher.launch({
  port: 9222,
  chromeFlags: [ '--headless' ]
}).then(function(chrome) {

  setTimeout(() => chrome.kill(), 1000);
});
```

- `require('chrome-remote-interface')` - [lib:Chrome-Remote-Interface library](/chrome-headless/how-to-install-chrome-remote-interface) to operate
- `require('chrome-launcher')` - [lib:Chrome-Launcher library](/chrome-headless/how-to-install-chrome-launcher-library) to start/stop Chrome browser programmatically
- `chromeLauncher.launch` - launch Chrome with specified params
- `port: 9222` - remote debugging protocol port
- `chrome.kill()` - close browser (or just press `Ctrl+C` in CLI)

group: cri


