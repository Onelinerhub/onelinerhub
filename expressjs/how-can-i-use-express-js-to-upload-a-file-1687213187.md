# How can I use Express.js to upload a file?
// plain

Express.js is a web application framework for Node.js that can be used for uploading files. To use Express.js to upload a file, you will need to install the Express.js package and create an Express.js application.

## Example code

```
const express = require('express');
const app = express();
const multer = require('multer');
const upload = multer({dest: 'uploads/'});

app.post('/upload', upload.single('myFile'), (req, res, next) => {
    const file = req.file
    if (!file) {
      const error = new Error('Please upload a file')
      error.httpStatusCode = 400
      return next(error)
    }
    res.send(file)
})

app.listen(3000, () => console.log('Server started'))
```

## Output example

```
Server started
```

The code above will create an Express.js application that will listen for POST requests on the '/upload' route. The multer package is used to handle the file upload. The `upload.single()` method is used to upload a single file, and the file is stored in the `uploads/` directory. The file is then sent in the response.

## Code explanation

- `const express = require('express');`: This line imports the Express.js package.
- `const app = express();`: This line creates the Express.js application.
- `const multer = require('multer');`: This line imports the multer package.
- `const upload = multer({dest: 'uploads/'});`: This line configures multer to store the uploaded file in the `uploads/` directory.
- `app.post('/upload', upload.single('myFile'), (req, res, next) => {...})`: This line listens for POST requests on the '/upload' route and uses the `upload.single()` method to upload a single file.
- `res.send(file)`: This line sends the file in the response.

## Helpful links
- [Express.js](https://expressjs.com/)
- [Multer](https://www.npmjs.com/package/multer)

onelinerhub: [How can I use Express.js to upload a file?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-to-upload-a-file-1687213187)