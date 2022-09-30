# How to write file

```js
const fs = require('fs');
fs.writeFile('/tmp/test.txt', 'hi!', (err, data) => {
  console.log(err);
});
```

- `require('fs')` - library to work with file system
- `/tmp/test.txt` - path of file to write
- `'hi!'` - Data to write to file
- `console.log(err)` - if `err` is not `null`, something wrong happened
- `fs.writeFile(` - writes given data to specified file

group: files

## Example: 
```js
const fs = require('fs');
fs.writeFile('/tmp/test.txt', 'hi!', (err, data) => {
  console.log(err);
});
```
```
null

```

link_youtube: https://youtu.be/2kY3WWq1ras
