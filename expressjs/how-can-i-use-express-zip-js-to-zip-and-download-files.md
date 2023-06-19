# How can I use express-zip js to zip and download files?
// plain

Express-zip is a library for Node.js that can be used to zip and download files. It provides a simple API for compressing files into a zip archive and streaming the archive to the client.

Here is an example of how to use express-zip to zip and download files.

```
const express = require('express');
const expressZip = require('express-zip');

const app = express();

app.get('/download', (req, res) => {
  const files = [
    { path: 'file1.txt', name: 'file1.txt' },
    { path: 'file2.txt', name: 'file2.txt' },
  ];
  res.zip(files, 'files.zip');
});

app.listen(3000);
```

This example will create a zip archive from two files, `file1.txt` and `file2.txt`, and stream it to the client.

Here is a breakdown of the code:

- `const express = require('express');`: Loads the Express.js library.
- `const expressZip = require('express-zip');`: Loads the Express-zip library.
- `const app = express();`: Creates an Express.js application.
- `app.get('/download', (req, res) => {`: Defines a route handler for the `GET /download` route.
- `const files = [`: Defines an array of files to be included in the zip archive.
- `res.zip(files, 'files.zip');`: Calls the `zip()` method to create the zip archive and stream it to the client.

For more information, see the [express-zip documentation](https://www.npmjs.com/package/express-zip).

onelinerhub: [How can I use express-zip js to zip and download files?](https://onelinerhub.com/expressjs/how-can-i-use-express-zip-js-to-zip-and-download-files)