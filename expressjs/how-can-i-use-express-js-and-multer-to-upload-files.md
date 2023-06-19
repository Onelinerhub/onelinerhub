# How can I use Express.js and Multer to upload files?
// plain

Express.js and Multer can be used together to upload files. Multer is a Node.js middleware for handling multipart/form-data, which is primarily used for uploading files.

## Example code

```js
const express = require('express');
const multer = require('multer');
const upload = multer({ dest: 'uploads/' });

const app = express();

app.post('/upload', upload.single('myFile'), (req, res, next) => {
  const file = req.file;
  if (!file) {
    const error = new Error('Please upload a file');
    error.httpStatusCode = 400;
    return next(error);
  }
  res.send(file);
});
```

This example code will create an Express.js application with a single route that will accept a single file upload. The file will be uploaded to the `uploads/` directory and the file will be sent back as a response.

## Code explanation

1. `const express = require('express');` - Require the Express.js module.
2. `const multer = require('multer');` - Require the Multer module.
3. `const upload = multer({ dest: 'uploads/' });` - Create a Multer instance with the destination folder set to `uploads/`.
4. `app.post('/upload', upload.single('myFile'), (req, res, next) => {` - Create a POST route for `/upload` and use the Multer instance to accept a single file upload named `myFile`.
5. `const file = req.file;` - Get the file from the request.
6. `if (!file) {` - Check if a file was uploaded.
7. `res.send(file);` - Send the file back as a response.

## Helpful links
- [Express.js](https://expressjs.com/)
- [Multer](https://github.com/expressjs/multer)

onelinerhub: [How can I use Express.js and Multer to upload files?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-and-multer-to-upload-files)