# How to get request header in HTTP server

```js
const http = require('http');

const server = http.createServer((req, res) => {
  res.end( req.headers['x-test'] );
});

server.listen(82, '127.0.0.1');
```

- `require('http')` - import module to work with `http` protocol
- `http.createServer` - creates HTTP server
- `(req,` - object with request data
- `res` - object to manage response
- `.end(` - finished `http` response with given content
- `req.headers` - object with all request headers
- `x-test` - sample request header to get value of

group: http_server

## Example: 
```js
curl -H "x-test: 1234" http://127.0.0.1:82/
```
```
1234
```

