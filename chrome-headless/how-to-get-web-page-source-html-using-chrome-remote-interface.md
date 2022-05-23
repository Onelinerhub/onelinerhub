# How to get web page source HTML using Chrome Remote Interface

### Execute this javascript file using `nodejs`:

```js
const chromeLauncher = require('chrome-launcher');
const CDP = require('chrome-remote-interface');

chromeLauncher.launch({ port: 9222, chromeFlags: [ '--headless' ] }).then(function(chrome) {
  CDP(async (client) => {
    const {Network, Page, Runtime} = client;
    await Page.enable();
    await Page.navigate({url: 'https://github.com'});
    await Page.loadEventFired();
    
    const result = await Runtime.evaluate({ expression: 'document.documentElement.outerHTML' });
    const html = result.result.value;
    console.log(html);
    
    await client.close();
    chrome.kill();
  });
});

```

- `require('chrome-launcher')` - [lib:Chrome-Launcher library](/chrome-headless/how-to-install-chrome-launcher-library) to start/stop Chrome browser programmatically
- `require('chrome-remote-interface')` - [lib:Chrome-Remote-Interface library](/chrome-headless/how-to-install-chrome-remote-interface) to operate
- `chromeLauncher.launch` - launch Chrome with specified params
- `Page.navigate` - go to specified URL
- `await Page.loadEventFired()` - wait while page is loaded
- `Runtime.evaluate` - execute given `JavaScript` expression
- `document.documentElement.outerHTML` - returns full page HTML
- `console.log(html)` - output HTML right into console

group: src

## Example: 
```js
nodejs test.js
```
```
<html lang="en" data-a11y-animated-images="system"><head>
    <meta charset="utf-8">
    ...
```

