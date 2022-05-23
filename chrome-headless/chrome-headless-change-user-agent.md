# How to change user agent using Chrome Remote Interface

```js
const chromeLauncher = require('chrome-launcher');
const CDP = require('chrome-remote-interface');

chromeLauncher.launch({ port: 9222, chromeFlags: [ '--headless' ] }).then(function(chrome) {
  CDP(async (client) => {
    const {Network, Page} = client;
    Network.setUserAgentOverride({'userAgent': 'MyBot2.0'});
    await Page.enable();
    await Page.navigate({url: 'https://github.com'});
    await Page.loadEventFired();
    
    // Do something when page loads
    
    await client.close();
    chrome.kill();
  });
});

```

- `require('chrome-launcher')` - [lib:Chrome-Launcher library](/chrome-headless/how-to-install-chrome-launcher-library) to start/stop Chrome browser programmatically
- `require('chrome-remote-interface')` - [lib:Chrome-Remote-Interface library](/chrome-headless/how-to-install-chrome-remote-interface) to operate
- `chromeLauncher.launch` - launch Chrome with specified params
- `Network.setUserAgentOverride` - allows setting custom user agent
- `MyBot2.0` - user agent value to use for page request
- `Page.navigate` - go to specified URL

group: user-agent


