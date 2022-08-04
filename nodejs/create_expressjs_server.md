# Static file server with Node.js and Express

```javascript
const express = require('express');
const path = require('path');

const app = express();
const port = 3000;

app.use(express.static('/var/www/files'));

app.get('/', (req, res) => {
  res.sendFile('/var/www/files/index.html');
});

app.listen(port);
```

- `app = express()` - create [Express](http://expressjs.com/) app
- `express.static` - server static files from given directory
- `/var/www/files` - path to static files root directory
- `app.listen` - launch app on specified port


