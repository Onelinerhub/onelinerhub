# How can I use Express.js to upload a file?
// plain

Express.js is a popular Node.js web application framework that can be used to upload files. The following code example demonstrates how to upload a file using Express.js.

```
const express = require('express');
const multer = require('multer');

const app = express();

// Set up multer to handle file uploads
const upload = multer({ dest: 'uploads/' });

// Handle POST request to upload a file
app.post('/upload', upload.single('myFile'), (req, res) => {
  const file = req.file;
  if (!file) {
    const error = new Error('Please upload a file');
    error.httpStatusCode = 400;
    return next(error);
  }
  res.send(file);
});

app.listen(3000);
```

The code above creates an Express.js application and uses the [Multer](https://github.com/expressjs/multer) middleware to handle file uploads. It sets up the `upload` middleware to store uploaded files in the `uploads/` directory and then handles a POST request to the `/upload` endpoint. The `upload.single('myFile')` part of the code tells Multer to expect a single file with the name `myFile` in the request. If the file is successfully uploaded, the `req.file` object will contain information about the uploaded file. The code then sends the file back as the response.

The following is a list of parts used in the code example above and their explanations:

- `const express = require('express')`: This line imports the Express.js module.
- `const multer = require('multer')`: This line imports the Multer module.
- `const upload = multer({ dest: 'uploads/' })`: This line sets up the Multer middleware to store uploaded files in the `uploads/` directory.
- `upload.single('myFile')`: This line tells Multer to expect a single file with the name `myFile` in the request.
- `req.file`: This object will contain information about the uploaded file if the upload is successful.
- `res.send(file)`: This line sends the file back as the response.

## Helpful links

- [Express.js Documentation](https://expressjs.com/)
- [Multer Documentation](https://github.com/expressjs/multer)

onelinerhub: [How can I use Express.js to upload a file?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-to-upload-a-file)