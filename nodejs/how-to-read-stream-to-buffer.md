# How to read stream to Buffer

```js
const fs = require('fs');
let input = fs.createReadStream('/var/www/examples/test.txt');

input.on('data', buf => {
  console.log(buf);
});
```

- `require('fs')` - library to work with file system
- `fs.createReadStream(` - create stream to read data from (file in our case)
- `/var/www/examples/test.txt` - path to file to stream read
- `.on('data'` - handle date reading from stream
- `buf` - buffer gets data chunk read from stream

group: streams

## Example: 
```js
const fs = require('fs');
let input = fs.createReadStream('/var/www/examples/test.txt');

input.on('data', buf => {
  console.log(buf);
});
```
```
<Buffer 68 69 21 0a>

```

link_youtube: https://youtu.be/tOXdMQvVOTk
