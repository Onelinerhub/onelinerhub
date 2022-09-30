# How to read stream to string

```js
const fs = require('fs');
let input = fs.createReadStream('/var/www/examples/test.txt');

const chunks = [];
input.on('data', buf => chunks.push(buf));
input.on('end', () => console.log( Buffer.concat(chunks).toString() ))
```

- `require('fs')` - library to work with file system
- `fs.createReadStream(` - create stream to read data from (file in our case)
- `/var/www/examples/test.txt` - path to file to stream read
- `.on('data'` - handle date reading from stream
- `chunks.push(buf)` - push each chunk into array
- `Buffer.concat(chunks)` - join all chunks into single buffer
- `.toString()` - convert Buffer to string
- `input.on('end'` - fire when stream reading was finished

group: streams

## Example: 
```js
const fs = require('fs');
let input = fs.createReadStream('/var/www/examples/test.txt');

const chunks = [];
input.on('data', buf => chunks.push(buf));
input.on('end', () => console.log( Buffer.concat(chunks).toString() ))
```
```
hi!


```

link_youtube: https://youtu.be/5TfDDDYR5Ws
