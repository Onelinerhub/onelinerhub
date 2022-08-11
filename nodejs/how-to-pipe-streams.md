# How to pipe streams

### You might want to use [`pipeline()`](https://onelinerhub.com/nodejs/how-to-pipeline-streams) as a better alternative that will properly clean memory after stream processing.

```js
const fs = require('fs');
let input = fs.createReadStream('/var/www/examples/test.txt');
let output = fs.createWriteStream('/tmp/out.txt');
input.pipe(output);
```

- `require('fs')` - library to work with file system
- `fs.createReadStream(` - create stream to read data from (file in our case)
- `fs.createWriteStream` - open file and create writing stream from it
- `/var/www/examples/test.txt` - path to file to stream read
- `/tmp/out.txt` - path to file to write stream to
- `.pipe(` - pipe `input` stream to `output` (in our case - read from input file and write to output)

group: streams

## Example: 
```js
const fs = require('fs');
let input = fs.createReadStream('/var/www/examples/test.txt');
let output = fs.createWriteStream('/tmp/out.txt');
input.pipe(output);
```

