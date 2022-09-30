# How to set content type in HTTP server

```js
const http = require('http');

const server = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/csv')
  res.end("1,2,3");
});

server.listen(82, '127.0.0.1');
```

- `require('http')` - import module to work with `http` protocol
- `http.createServer` - creates HTTP server
- `(req,` - object with request data
- `res` - object to manage response
- `.end(` - finished `http` response with given content
- `.setHeader(` - sets response header
- `Content-Type` - we're going to set content type
- `text/csv` - let's send `csv` content as example

group: http_server

## Example: 
```js
curl -i http://127.0.0.1:82/
```
```
HTTP/1.1 200 OK
Content-Type: text/csv
Date: Thu, 04 Aug 2022 13:46:46 GMT
Connection: keep-alive
Keep-Alive: timeout=5
Content-Length: 5

1,2,3
```

link_youtube: https://youtu.be/_4vifQUESCI
