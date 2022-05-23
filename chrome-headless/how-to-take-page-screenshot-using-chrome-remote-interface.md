# How to take page screenshot using Chrome Remote Interface

```js
const chromeLauncher = require('chrome-launcher');
const CDP = require('chrome-remote-interface');
const fs = require('fs');

chromeLauncher.launch({ port: 9222, chromeFlags: [ '--window-size=400,800', '--headless' ] }).then(function(chrome) {

  CDP(async (client) => {
    const {Page} = client;
    await Page.enable();
    await Page.navigate({url: 'https://github.com'});
    await Page.loadEventFired();
    const {data} = await Page.captureScreenshot();
    fs.writeFileSync('screen.png', Buffer.from(data, 'base64'));
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
- `await Page.loadEventFired()` - wait while page is loaded
- `Page.captureScreenshot` - make screenshot
- `screen.png` - path to save screenshot to
- `client.close` - close remote debugging interface connection
- `chrome.kill()` - close browser

group: screenshot


