# How to pipeline streams

```js
const fs = require('fs');
const { pipeline } = require('stream');

let input = fs.createReadStream('/var/www/examples/test.txt');
let output = fs.createWriteStream('/tmp/out.txt');

pipeline(input, output, (err) => console.log(err));
```

- `require('fs')` - library to work with file system
- `fs.createReadStream(` - create stream to read data from (file in our case)
- `fs.createWriteStream` - open file and create writing stream from it
- `/var/www/examples/test.txt` - path to file to stream read
- `/tmp/out.txt` - path to file to write stream to
- `pipeline` - pipelines given streams (left to right) and properly destroys all objects after processing
- `(err) => console.log(err)` - last argument of `pipeline()` is always error callback

group: streams

## Example: 
```js
const fs = require('fs');
const { pipeline } = require('stream');

let input = fs.createReadStream('/var/www/examples/test.txt');
let output = fs.createWriteStream('/tmp/out.txt');
pipeline(input, output, (err) => console.log(err));
```
```
undefined

```

link_youtube: https://youtu.be/H3rJM6gOFlE
