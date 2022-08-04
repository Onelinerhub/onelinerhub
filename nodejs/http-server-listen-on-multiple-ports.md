# HTTP server listen on multiple ports

```js
const http = require('http');

[81,82,83].forEach(function(p) {
  let server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.end('Hi');
  });
  
  server.listen(p);
})
```

- `require('http')` - import module to work with `http` protocol
- `http.createServer` - creates HTTP server
- `(req,` - object with request data
- `res` - object to manage response
- `.end(` - finished `http` response with given content
- `server.listen` - launch server on a given port and hostname
- `[81,82,83]` - array of ports to listen server on

group: http_server

## Example: 
```js
curl http://127.0.0.1:81/
curl http://127.0.0.1:82/
curl http://127.0.0.1:83/
```
```
Hi
Hi
Hi
```

