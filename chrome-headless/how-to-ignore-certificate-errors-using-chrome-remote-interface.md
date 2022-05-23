# How to ignore certificate errors using Chrome Remote Interface

```js
const chromeLauncher = require('chrome-launcher');
const CDP = require('chrome-remote-interface');

chromeLauncher.launch({
  port: 9222,
  chromeFlags: [ '--window-size=400,800', '--headless' ]
}).then(function(chrome) {

  CDP(async (client) => {
    const {Page, Security} = client;
  
    Security.certificateError(({eventId}) => {
      Security.handleCertificateError({ eventId, action: 'continue' });
    });
  
    await Page.enable();
    await Security.enable();
    await Security.setOverrideCertificateErrors({override: true});
    await Page.enable();
    await Page.navigate({url: 'https://github.com'});
    await Page.loadEventFired();
  
    // Do something with loaded page here
    
    await client.close();
    chrome.kill();
  });
});
```

- `require('chrome-remote-interface')` - [lib:Chrome-Remote-Interface library](/chrome-headless/how-to-install-chrome-remote-interface) to operate
- `require('chrome-launcher')` - [lib:Chrome-Launcher library](/chrome-headless/how-to-install-chrome-launcher-library) to start/stop Chrome browser programmatically
- `chromeLauncher.launch` - launch Chrome with specified params
- `CDP(async (client)` - init remote debugging interface connection when browser is ready
- `Security.certificateError` - create listener for certificate errors
- `Security.setOverrideCertificateErrors` - enable certificate errors override to use our custom handler
- `Page.navigate` - go to specified URL
- `await Page.loadEventFired()` - wait while page is loaded
- `client.close` - close remote debugging interface connection
- `chrome.kill()` - close browser


