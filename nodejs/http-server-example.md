# HTTP server example

```js
const http = require('http');

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.end('Hi');
});

server.listen(82, '127.0.0.1');
```

- `require('http')` - import module to work with `http` protocol
- `http.createServer` - creates HTTP server
- `req` - object with request data
- `res` - object to manage response
- `statusCode` - sets `http` status code to `200` (response is ok)
- `.end(` - finished `http` response with given content
- `server.listen` - launch server on a given port and hostname
- `82` - port to listen on
- `127.0.0.1` - address to listen on

group: http_server

## Example: 
```js
curl http://127.0.0.1:82/
```
```
Hi
```

