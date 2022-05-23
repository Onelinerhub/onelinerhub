# How to trigger mouse click in headless mode

### Execute this javascript file using `nodejs`:

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
    
    const options = { x: 350, y: 20, button: 'left', clickCount: 1 };
    Promise.resolve().then(() => {
      options.type = 'mousePressed';
      return client.Input.dispatchMouseEvent(options);
    }).then(() => {
      options.type = 'mouseReleased';
      return client.Input.dispatchMouseEvent(options);
    });
    
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
- `const options` - define options for mouse event (coordinates are targeted on right menu)
- `mousePressed` - first send this event
- `mouseReleased` - then tell chrome mouse was released
- `Page.captureScreenshot()` - capture screenshot to check if mouse was really clicked and browser reacted


