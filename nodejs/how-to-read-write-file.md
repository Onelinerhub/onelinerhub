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

