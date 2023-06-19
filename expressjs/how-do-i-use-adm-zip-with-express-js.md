# How do I use adm-zip with Express.js?
// plain

Adm-zip is a Node.js module that allows you to create, read and extract zip files. It can be used with Express.js to zip files and folders for download.

To use adm-zip with Express.js, you need to install it as a dependency:

```
npm install adm-zip
```

Then, you can require it and use it in your Express.js code:

```javascript
const express = require('express');
const AdmZip = require('adm-zip');

const app = express();

app.get('/download', (req, res, next) => {
  const zip = new AdmZip();
  zip.addFile('file1.txt', Buffer.alloc(30), 'Some content for file 1');
  zip.addFile('file2.txt', Buffer.alloc(30), 'Some content for file 2');
  const zipData = zip.toBuffer();

  res.set('Content-Type', 'application/zip');
  res.set('Content-Length', zipData.length);
  res.set('Content-Disposition', 'attachment; filename=files.zip');
  res.send(zipData);
});

app.listen(3000);
```

This code creates a new `AdmZip` object, adds two files to it and converts it to a buffer. Then, it sets the response headers and sends the zip file.

## Code explanation


1. Install adm-zip: `npm install adm-zip`
2. Require adm-zip: `const AdmZip = require('adm-zip');`
3. Create a new `AdmZip` object: `const zip = new AdmZip();`
4. Add files to the zip object: `zip.addFile('file1.txt', Buffer.alloc(30), 'Some content for file 1');`
5. Convert the zip object to a buffer: `const zipData = zip.toBuffer();`
6. Set response headers: `res.set('Content-Type', 'application/zip');`
7. Send the buffer: `res.send(zipData);`

## Helpful links

- [adm-zip on npm](https://www.npmjs.com/package/adm-zip)
- [adm-zip on GitHub](https://github.com/cthackers/adm-zip)

onelinerhub: [How do I use adm-zip with Express.js?](https://onelinerhub.com/expressjs/how-do-i-use-adm-zip-with-express-js)