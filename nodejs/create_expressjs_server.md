# Static file server example with Node.js and Express.

requires [Node.js](https://nodejs.org/en/) and [Express](https://expressjs.com/) installed

```javascript
const express = require('express');
const path = require('path');

const app = express();
const port = 3000;

app.use(express.static(path.join(__dirname + '/files')));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname + '/files/index.html'));
});

app.listen(port, () => {
  console.log(`Express started on port ${port}`);
});
```

- /files - location on server that holds the static files
- __dirname - absolute path of the directory containing executing file
- app.get('/' - defines what static file to serve at home url routing
