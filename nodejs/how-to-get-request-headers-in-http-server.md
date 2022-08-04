# How to send JSON response from HTTP server

```js
const http = require('http');

const server = http.createServer((req, res) => {
  let data = {name: 'Joe', age: 98};
  res.setHeader('Content-Type', 'application/json')
  res.end(JSON.stringify(data));
});

server.listen(82, '127.0.0.1');
```

- `require('http')` - import module to work with `http` protocol
- `http.createServer` - creates HTTP server
- `(req,` - object with request data
- `res` - object to manage response
- `.end(` - finished `http` response with given content
- `application/json` - set response content type to let client know we're sending `JSON`
- `JSON.stringify` - convert given object to JSON string

group: http_server

## Example: 
```js
curl -i http://127.0.0.1:82/
```
```
HTTP/1.1 200 OK
Content-Type: application/json
Date: Thu, 04 Aug 2022 12:34:32 GMT
Connection: keep-alive
Keep-Alive: timeout=5
Content-Length: 23

{"name":"Joe","age":98}
```

