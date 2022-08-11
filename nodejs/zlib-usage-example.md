# Zlib usage example

```js
const zlib = require('zlib');
const fs = require('fs');
const gzip = zlib.createGzip();
const inp = fs.createReadStream('/var/www/examples/test.txt');
const out = fs.createWriteStream('/tmp/test.gz');  
inp.pipe(gzip).pipe(out);
```

- `require('zlib')` - includes lib to work with compression
- `zlib.createGzip()` - creates new Gzip compression object
- `require('fs')` - library to work with file system
- `fs.createReadStream(` - create stream to read data from (file in our case)
- `fs.createWriteStream(` - create stream to write resulting (compressed) data to (file in our case)
- `.pipe(` - pipe object to the given stream
- `inp.pipe(gzip)` - pipes reading stream to gzip object (compress)
- `.pipe(out)` - then pipes compressed data to output stream (resulting `/tmp/test.gz` file)

group: zlib

## Example: 
```js
const zlib = require('zlib');  
const gzip = zlib.createGzip();  
const fs = require('fs');  
const inp = fs.createReadStream('/var/www/examples/test.txt');  
const out = fs.createWriteStream('/tmp/test.gz');  
inp.pipe(gzip).pipe(out);
```

