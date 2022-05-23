# How to wait for page load in headless mode

### In order to make sure page is loaded, use `nodejs` and [`Chrome Remote Interface`](/chrome-headless/how-to-install-chrome-remote-interface) library:

```js
const chromeLauncher = require('chrome-launcher');
const CDP = require('chrome-remote-interface');

chromeLauncher.launch({ port: 9222, chromeFlags: [ '--headless' ] }).then(function(chrome) {

  CDP(async (client) => {
    const {Page} = client;
    await Page.enable();
    await Page.navigate({url: 'https://onelinerhub.com'});
    await Page.loadEventFired();
    
    // page is loaded completely, do something here
    
    await client.close();
    chrome.kill();
  });
});
```

- `require('chrome-launcher')` - [lib:Chrome-Launcher library](/chrome-headless/how-to-install-chrome-launcher-library) to start/stop Chrome browser programmatically
- `require('chrome-remote-interface')` - [lib:Chrome-Remote-Interface library](/chrome-headless/how-to-install-chrome-remote-interface) to operate
- `chromeLauncher.launch` - launch Chrome with specified params
- `CDP(async (client)` - init remote debugging interface connection when browser is ready
- `Page.navigate` - go to specified URL
- `await Page.loadEventFired()` - wait for complete page load
- `client.close` - close remote debugging interface connection
- `chrome.kill()` - close browser


