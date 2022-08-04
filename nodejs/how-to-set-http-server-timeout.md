# How to set HTTP server timeout

```js
const http = require('http');

const server = http.createServer((req, res) => {
  req.setTimeout(5 * 1000);
  res.end('Hi');
});

server.listen(82);
```

- `require('http')` - import module to work with `http` protocol
- `http.createServer` - creates HTTP server
- `(req,` - object with request data
- `res` - object to manage response
- `req.setTimeout` - sets request timeout
- `5 * 1000` - timeout is set to 5 seconds (`5000` milliseconds)

group: http_server

## Example: 
```js
curl http://127.0.0.1:82/
```
```
Hi
```

