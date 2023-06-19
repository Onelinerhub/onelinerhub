# How do I delete a file using Express.js?
// plain

To delete a file using Express.js, you can use the `fs.unlink()` method. This method takes the path of the file to be deleted as its argument. The code below shows an example of how to use it:

```
// Import the filesystem module
const fs = require('fs');

// Path of the file to be deleted
const filePath = '/path/to/file.txt';

// Delete the file
fs.unlink(filePath, (err) => {
  if (err) throw err;
  console.log(`${filePath} was deleted`);
});
```

## Output example


```
/path/to/file.txt was deleted
```

The code above consists of the following parts:

1. `const fs = require('fs')` imports the filesystem module.
2. `const filePath = '/path/to/file.txt'` specifies the path of the file to be deleted.
3. `fs.unlink(filePath, (err) => {...})` calls the `fs.unlink()` method, which takes the path of the file to be deleted as its argument.
4. `if (err) throw err` checks if an error occurred and throws it if it did.
5. `console.log(`${filePath} was deleted`)` logs a message to the console indicating that the file was deleted.

For more information on deleting files using Express.js, see the following links:

- [Node.js File System Module](https://nodejs.org/api/fs.html)
- [How to Delete a File in Node.js](https://www.tutorialsteacher.com/nodejs/nodejs-delete-file)

onelinerhub: [How do I delete a file using Express.js?](https://onelinerhub.com/expressjs/how-do-i-delete-a-file-using-express-js)