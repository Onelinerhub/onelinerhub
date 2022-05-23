# Chrome Remote Interface usage example

```js
const chromeLauncher = require('chrome-launcher');
const CDP = require('chrome-remote-interface');
const fs = require('fs');

chromeLauncher.launch({
  port: 9222,
  chromeFlags: [ '--window-size=400,800', '--headless' ]
}).then(function(chrome) {

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

- `require('chrome-remote-interface')` - [lib:CHrome-Remote-Interface library](/chrome-headless/how-to-install-chrome-remote-interface) to operate
- `require('chrome-launcher')` - asd

group: cri


