# How to log to file

```js
const fs = require('fs');

const logger = new console.Console({
  stdout: fs.createWriteStream('/tmp/out.log'),
  stderr: fs.createWriteStream('/tmp/err.log')
});

logger.log('hi, I am message');
logger.error('I AM ERROR HA HA HA');
```

- `require('fs')` - library to work with file system
- `new console.Console` - create new Console object to log data
- `fs.createWriteStream` - open file and create writing stream from it
- `stdout` - set stream (file) to write standard messages to
- `stderr` - set stream (file) to write errors to
- `logger.log` - log standard message
- `logger.error` - log error

group: log

## Example: 
```js
cat /tmp/err.log
```
```
I AM ERROR HA HA HA
```

