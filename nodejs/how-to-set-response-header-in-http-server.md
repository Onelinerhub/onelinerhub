# How to set response header in HTTP server

```js
const http = require('http');

const server = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain')
  res.end();
});

server.listen(82, '127.0.0.1');
```

- `require('http')` - import module to work with `http` protocol
- `http.createServer` - creates HTTP server
- `(req,` - object with request data
- `res` - object to manage response
- `.end(` - finished `http` response with given content
- `.setHeader(` - sets response header
- `Content-Type` - name of the header to send
- `text/plain` - value of the header to send

group: http_server

## Example: 
```js
curl -i http://127.0.0.1:82/
```
```
HTTP/1.1 200 OK
Content-Type: text/plain
Date: Thu, 04 Aug 2022 12:33:39 GMT
Connection: keep-alive
Keep-Alive: timeout=5
Content-Length: 0
```

