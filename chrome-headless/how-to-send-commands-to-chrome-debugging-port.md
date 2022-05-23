# How to send commands to Chrome debugging port

### In order to keep running, we should enable [debugging port](/), so Chrome knows we want it to stay:

```js
const CDP = require('chrome-remote-interface');

CDP(async (client) => {
  const {Page} = client;
  await Page.enable();
  await Page.navigate({url: 'https://onelinerhub.com'});
  await Page.loadEventFired();
  
  console.log('page is loaded, ok');
  
  await client.close();
});

```

- `require('chrome-remote-interface')` - [lib:Chrome-Remote-Interface library](/chrome-headless/how-to-install-chrome-remote-interface) to operate
- `CDP(async (client)` - init remote debugging interface connection when browser is ready
- `Page.navigate` - go to specified URL
- `await Page.loadEventFired()` - wait while page is loaded
- `console.log` - print some text to console (add code to manipulate Chrome here)
- `client.close` - close remote debugging interface connection

group: remote-debugging


