# How do I download a zip file using Express.js?
// plain

To download a zip file using Express.js, you need to use the [`res.download()`](https://expressjs.com/en/api.html#res.download) function.

The code below shows an example of how to use `res.download()` to download a zip file.

```javascript
// Import the Express module
const express = require('express');

// Create an Express application
const app = express();

// Create a route
app.get('/download', (req, res) => {
  // Set the file path
  const filePath = './myZipFile.zip';
  // Set the file name
  const fileName = 'myZipFile.zip';

  // Use res.download() to download the file
  res.download(filePath, fileName);
});

// Start the server
app.listen(3000, () => console.log('Server listening on port 3000!'));
```

The output of the code above will be:

```
Server listening on port 3000!
```

When a request is made to `http://localhost:3000/download`, the file `myZipFile.zip` will be downloaded.

## Code explanation


1. `require('express')`: This imports the Express module.
2. `const app = express()`: This creates an Express application.
3. `app.get('/download', (req, res) => { ... })`: This creates a route which will handle the download request.
4. `const filePath = './myZipFile.zip'`: This sets the file path of the zip file.
5. `const fileName = 'myZipFile.zip'`: This sets the file name of the zip file.
6. `res.download(filePath, fileName)`: This uses the Express `res.download()` function to download the zip file.
7. `app.listen(3000, () => console.log('Server listening on port 3000!'))`: This starts the server on port 3000.

onelinerhub: [How do I download a zip file using Express.js?](https://onelinerhub.com/expressjs/how-do-i-download-a-zip-file-using-express-js)