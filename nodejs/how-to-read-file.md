# How to read file

```js
const fs = require('fs');

fs.readFile("/tmp/test.txt", "utf8", (err, data) => {
  console.log(data);
});
```

- `fs.readFile()` - reads file and returns data in callback function
- `/tmp/test.txt` - path to [text file](https://onelinerhub.com/nodejs/how-to-read-write-file) to read
- `utf8` - encoding to read text in
- `console.log(data)` - log `date` from file to console

group: files

## Example: 
```js
const fs = require('fs');

fs.readFile("/tmp/test.txt", "utf8", (err, data) => {
  console.log(data);
});
```
```
hi!

```

