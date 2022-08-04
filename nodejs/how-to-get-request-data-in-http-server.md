# How to get request data in HTTP server

```js
const http = require('http');

const server = http.createServer((req, res) => {
  let data = '';
  req.on('data', chunk => {
    data += chunk;
  });

  req.on('end', () => {
    res.end(data);
  });
});

server.listen(82, '127.0.0.1');
```

- `require('http')` - import module to work with `http` protocol
- `http.createServer` - creates HTTP server
- `req.on(` - handle specific http event
- `on('data'` - handle data receiving with specified callback
- `data += chunk` - collect all post data chunks into single `data` variable
- `on('end'` - handle event when request has finished
- `res.end(data);` - send data in response to client and finish
- `server.listen` - launch server on a given port and hostname

group: http_server

## Example: 
```js
curl http://127.0.0.1:82/ --data "123"
```
```
123
```

