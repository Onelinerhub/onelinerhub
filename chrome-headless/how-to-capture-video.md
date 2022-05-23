# How to capture video

```js
const chromeLauncher = require('chrome-launcher');
const CDP = require('chrome-remote-interface');
const fs = require('fs');

chromeLauncher.launch({ port: 9222, chromeFlags: [ '--window-size=1280,720', '--headless' ] }).then(function(chrome) {
  CDP(async (client) => {
    const {Page} = client;

    await Page.enable();
    await Page.navigate({url: 'https://github.com'});
    await Page.loadEventFired();
    await Page.startScreencast({format: 'png', everyNthFrame: 1});
    
    let counter = 0;
    while(counter < 25){
      const {data, metadata, sessionId} = await Page.screencastFrame();
      await Page.screencastFrameAck({sessionId: sessionId});
      
      fs.writeFileSync('screen-' + counter + '.png', Buffer.from(data, 'base64'));
      counter += 1;

      console.log(metadata.timestamp);
    }
    
    await client.close();
    chrome.kill();
  });
});

```

- `require('chrome-launcher')` - [lib:Chrome-Launcher library](/chrome-headless/how-to-install-chrome-launcher-library) to start/stop Chrome browser programmatically
- `require('chrome-remote-interface')` - [lib:Chrome-Remote-Interface library](/chrome-headless/how-to-install-chrome-remote-interface) to operate
- `Page.startScreencast` - starts screen cast process in `PNG` format
- `Page.screencastFrame` - get generated screen cast frame
- `fs.writeFileSync` - save given screen frame buffer to file
- `'screen-' + counter + '.png'` - use file name with counter variable to generate sequence of images
- `client.close` - close remote debugging interface connection
- `chrome.kill()` - close browser


