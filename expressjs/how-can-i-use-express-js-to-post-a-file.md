# How can I use Express.js to post a file?
// plain

Express.js is a web application framework for Node.js that enables you to create a server-side application. You can use Express.js to post a file by using the `multer` middleware.

```
const express = require('express');
const multer = require('multer');

const app = express();

const upload = multer({
  dest: 'uploads/'
});

app.post('/upload', upload.single('file'), (req, res) => {
  console.log(req.file);
  res.send('File uploaded successfully');
});
```

The example code above creates an Express application with the `multer` middleware. The `multer` middleware is used to parse the file that is uploaded. The `upload.single('file')` function is used to specify the name of the file that is being uploaded. The `req.file` object is used to get the information about the file that was uploaded. The `res.send` function is used to send a response to the client.

Parts of the code:
- `const express = require('express')`: This line imports the Express module into the application.
- `const multer = require('multer')`: This line imports the multer module into the application.
- `app.post('/upload', upload.single('file'), (req, res) => {`: This line creates a POST route that is used to handle the file upload.
- `upload.single('file')`: This line specifies the name of the file that is being uploaded.
- `req.file`: This object is used to get the information about the file that was uploaded.
- `res.send('File uploaded successfully')`: This line sends a response to the client.

## Helpful links
- [Express.js](https://expressjs.com/)
- [Multer](https://www.npmjs.com/package/multer)

onelinerhub: [How can I use Express.js to post a file?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-to-post-a-file)