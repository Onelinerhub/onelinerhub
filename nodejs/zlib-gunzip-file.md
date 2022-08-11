# Zlib gunzip file

```js
const zlib = require('zlib');
const fs = require('fs');
const f = fs.readFileSync('/tmp/test.gz');  
zlib.gunzip(f, (err, bin) => {
  console.log(bin.toString())
})
```

- `require('zlib')` - includes lib to work with compression
- `require('fs')` - library to work with file system
- `.readFileSync(` - return content from given file
- `/tmp/test.gz` - path to gzipped file
- `.gunzip(` - decompress gzipped data
- `bin.toString()` - convert uncompressed buffer to string

group: zlib

## Example: 
```js
const zlib = require('zlib');
const fs = require('fs');
const f = fs.readFileSync('/tmp/test.gz');  
zlib.gunzip(f, (err, bin) => {
  console.log(bin.toString())
})
```
```
hi!


```

