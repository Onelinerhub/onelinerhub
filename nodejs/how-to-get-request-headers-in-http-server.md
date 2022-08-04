# How to get request headers in HTTP server

```js
const http = require('http');

const server = http.createServer((req, res) => {
  console.log(req.headers['x-test']);
  res.end();
});

server.listen(82, '127.0.0.1');
```

- `require('http')` - import module to work with `http` protocol
- `http.createServer` - creates HTTP server
- `(req,` - object with request data
- `res` - object to manage response
- `.end(` - finished `http` response with given content
- `req.headers` - object

group: http_server


