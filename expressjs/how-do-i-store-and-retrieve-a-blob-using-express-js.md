# How do I store and retrieve a blob using Express.js?
// plain

Storing and retrieving a blob using Express.js is a relatively simple process.

First, you need to install the `multer` package which provides a middleware for handling multipart/form-data, which is necessary for uploading files.

```
$ npm install --save multer
```

Once installed, you can create a route in your Express app to handle the file upload.

```javascript
const multer = require('multer');

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, './uploads');
  },
  filename: (req, file, cb) => {
    cb(null, `${file.fieldname}-${Date.now()}`);
  },
});

const upload = multer({ storage });

app.post('/upload', upload.single('myFile'), (req, res) => {
  // req.file is the `myFile` file
  // req.body will hold the text fields, if there were any
});
```

To retrieve the blob, you can simply create a route in your Express app that serves the file.

```javascript
app.get('/uploads/:file', (req, res) => {
  const file = req.params.file;
  const filePath = path.join(__dirname, 'uploads', file);
  res.download(filePath);
});
```

The parts of the code are:

1. `multer` package installation - `$ npm install --save multer`
2. File upload route - creates a route to handle the file upload, using `multer` and `diskStorage`
3. File retrieval route - creates a route to serve the file

## Helpful links

- [Multer](https://www.npmjs.com/package/multer)
- [Express File Uploads](https://expressjs.com/en/resources/middleware/multer.html)

onelinerhub: [How do I store and retrieve a blob using Express.js?](https://onelinerhub.com/expressjs/how-do-i-store-and-retrieve-a-blob-using-express-js)