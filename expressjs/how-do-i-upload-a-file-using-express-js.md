# How do I upload a file using Express.js?
// plain

To upload a file using Express.js, you can use the [`multer`](https://www.npmjs.com/package/multer) middleware. It is a node.js middleware for handling multipart/form-data, which is primarily used for uploading files.

Here is an example of how to use `multer`:

```javascript
// Require the multer module
const multer = require('multer');

// Initialize the multer middleware
const upload = multer({ dest: 'uploads/' });

// Create a route that will handle the file upload
app.post('/upload', upload.single('myFile'), (req, res) => {
  // Access the file that was uploaded
  const file = req.file;
  console.log(file);

  /*
  Output:
  {
    fieldname: 'myFile',
    originalname: 'example.jpg',
    encoding: '7bit',
    mimetype: 'image/jpeg',
    destination: 'uploads/',
    filename: 'd78c2acfb3f3a08d2a9f3c2cacb6e3f8',
    path: 'uploads/d78c2acfb3f3a08d2a9f3c2cacb6e3f8',
    size: 955941
  }
  */
});
```

The `multer` middleware will parse the multipart/form-data request, and store the file in the directory specified by the `dest` option. The `req.file` object will contain information about the uploaded file.

## Code explanation


- `const multer = require('multer');` - Require the `multer` module.
- `const upload = multer({ dest: 'uploads/' });` - Initialize the `multer` middleware with the `dest` option set to `uploads/`.
- `app.post('/upload', upload.single('myFile'), (req, res) => {` - Create a route that will handle the file upload, using the `upload.single()` method with the `myFile` parameter.
- `const file = req.file;` - Access the file that was uploaded.

## Helpful links

- [Multer](https://www.npmjs.com/package/multer) - npm package for handling multipart/form-data.

onelinerhub: [How do I upload a file using Express.js?](https://onelinerhub.com/expressjs/how-do-i-upload-a-file-using-express-js)