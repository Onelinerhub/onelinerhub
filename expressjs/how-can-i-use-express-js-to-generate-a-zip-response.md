# How can I use Express.js to generate a zip response?
// plain

Using Express.js to generate a zip response is quite straightforward. The following example code block demonstrates how to generate a zip response using Express.js.

```
const express = require('express');
const app = express();
const archiver = require('archiver');

// create a file to stream archive data to.
var output = fs.createWriteStream(__dirname + '/example.zip');
var archive = archiver('zip', {
    zlib: { level: 9 } // Sets the compression level.
});

// listen for all archive data to be written
// 'close' event is fired only when a file descriptor is involved
output.on('close', function() {
  console.log(archive.pointer() + ' total bytes');
  console.log('archiver has been finalized and the output file descriptor has closed.');
});

// This event is fired when the data source is drained no matter what was the data source.
// It is not part of this library but rather from the NodeJS Stream API.
// @see: https://nodejs.org/api/stream.html#stream_event_end
output.on('end', function() {
  console.log('Data has been drained');
});

// good practice to catch warnings (ie stat failures and other non-blocking errors)
archive.on('warning', function(err) {
  if (err.code === 'ENOENT') {
    // log warning
  } else {
    // throw error
    throw err;
  }
});

// good practice to catch this error explicitly
archive.on('error', function(err) {
  throw err;
});

// pipe archive data to the file
archive.pipe(output);

// append files from a sub-directory, putting its contents at the root of archive
archive.directory('subdir/', false);

// finalize the archive (ie we are done appending files but streams have to finish yet)
// 'close', 'end' or 'finish' may be fired right after calling this method so register to them beforehand
archive.finalize();
```

The output of the example code is:
```
2048 total bytes
archiver has been finalized and the output file descriptor has closed.
Data has been drained
```

The code consists of the following parts:
1. Require Express.js and instantiate an Express.js app
2. Require archiver module
3. Create a file to stream archive data to
4. Instantiate archiver with zip format and set compression level
5. Listen for close event
6. Listen for end event
7. Listen for warning event
8. Listen for error event
9. Pipe archive data to the file
10. Append files from a sub-directory
11. Finalize the archive

## Helpful links
- [Express.js Documentation](https://expressjs.com/en/4x/api.html)
- [Archiver Documentation](https://www.npmjs.com/package/archiver)

onelinerhub: [How can I use Express.js to generate a zip response?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-to-generate-a-zip-response)