# How to allow CORS in HTTP server

```js
const http = require('http');

const server = http.createServer((req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'OPTIONS, GET');
  res.setHeader('Access-Control-Max-Age', 60*60*24*30);
  
  res.end('Hi');
});

server.listen(82);
```

- `require('http')` - import module to work with `http` protocol
- `http.createServer` - creates HTTP server
- `(req,` - object with request data
- `res` - object to manage response
- `setHeader(` - sets response header
- `Access-Control-` - CORS headers to set
- `'*'` - allow access from all origins
- `60*60*24*30` - ACL lifetime is set to 30 days

group: http_server

## Example: 
```js
curl -i http://127.0.0.1:82/
```
```
HTTP/1.1 200 OK
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: OPTIONS, GET
Access-Control-Max-Age: 2592000
Date: Thu, 04 Aug 2022 12:20:44 GMT
Connection: keep-alive
Keep-Alive: timeout=5
Content-Length: 2

Hi
```

