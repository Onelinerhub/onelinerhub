# How can I configure Express.js to use IPv6?
// plain

Express.js is a web application framework for Node.js. It can be configured to use IPv6. To do this, you will need to use the Express.js `listen` method.

For example:

```
const express = require('express');
const app = express();

app.listen(3000, '::', function() {
  console.log('Listening on IPv6 port 3000!');
});
```

This will output:
```
Listening on IPv6 port 3000!
```

The `listen` method takes three parameters:

1. The port number to listen on (`3000` in this example).
2. The IPv6 address to listen on (`::` in this example).
3. A callback function to be called when the server is listening (`function() { console.log('Listening on IPv6 port 3000!'); }` in this example).

You can also use the `listen` method to listen on multiple ports and/or IPv4 and IPv6 addresses. For more information about the `listen` method, please refer to the Express.js [documentation](https://expressjs.com/en/api.html#app.listen).

onelinerhub: [How can I configure Express.js to use IPv6?](https://onelinerhub.com/expressjs/how-can-i-configure-express-js-to-use-ipv-)