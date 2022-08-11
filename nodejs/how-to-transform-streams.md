# How to use transform streams

```js
const fs = require('fs');
const { Transform } = require("stream");

let input = fs.createReadStream('/var/www/examples/test.txt');

const my_transform = new Transform({
  transform(chunk, encoding, callback) {
    callback(null, 'TRANSFORMED: ' + chunk.toString());
  },
});

my_transform.on('data', buf => console.log(buf.toString()));

input.pipe(my_transform);
```

- `require('fs')` - library to work with file system
- `fs.createReadStream(` - create stream to read data from (file in our case)
- `new Transform(` - create new stream that transforms data
- `transform(chunk, encoding, callback)` - chunk transformation function
- `'TRANSFORMED: ' + chunk.toString()` - return transformed chunk to callback (we add `TRANSFORMED:` text to chunk as transformation example)
- `.on('data'` - handle date reading from stream
- `.pipe(` - pipe object to the given stream (read from file and pipe to transforming stream)

group: streams

## Example: 
```js
const fs = require('fs');
const { Transform } = require("stream");

let input = fs.createReadStream('/var/www/examples/test.txt');

const my_transform = new Transform({
  transform(chunk, encoding, callback) {
    callback(null, 'TRANSFORMED: ' + chunk.toString());
  },
});

my_transform.on('data', buf => console.log(buf.toString()));

input.pipe(my_transform);
```
```
TRANSFORMED: hi!


```

