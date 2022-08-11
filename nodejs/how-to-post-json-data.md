# How to POST JSON data

```js
const https = require('https');

let data = JSON.stringify({a: 1, name: 'Joe'});

let req = https.request({
  hostname: 'echoof.me',
  port: 443,
  path: '/',
  method: 'POST',
  headers: {
    'Content-Length': data.length,
    'Content-type': 'application/json'
  }
}, (resp) => {
  let data = '';
  resp.on('data', (chunk) => { data += chunk; });

  resp.on('end', () => {
    console.log(data);
  });
});

req.write(data);
```

- `require('https')` - standard library to do `HTTP` requests
- `https.request(` - create new HTTP request
- `method: 'POST'` - ask Nodejs to make `POST` request
- `{a: 1, name: 'Joe'}` - sample JSON data to post
- `'Content-Length': data.length` - we need to send posted content length to the server
- `resp.on('data'` - handle response in chunks
- `(chunk) => { data += chunk; }` - collect all response chunks into single string
- `resp.on('end'` - fired when response ended
- `console.log(data);` - outputs full response from given URL
- `req.write(data)` - write `data` to given request (post `data` contents)

group: http_request

## Example: 
```js
const https = require('https');

let data = JSON.stringify({a: 1, name: 'Joe'});

let req = https.request({
  hostname: 'echoof.me',
  port: 443,
  path: '/',
  method: 'POST',
  headers: {
    'Content-Length': data.length,
    'Content-type': 'application/json'
  }
}, (resp) => {
  let data = '';
  resp.on('data', (chunk) => { data += chunk; });

  resp.on('end', () => {
    console.log(data);
  });
});

req.write(data);
```
```
IP:                           135.181.98.214

CONNECTION:                   close
CONTENT_TYPE:                 application/json
CONTENT_LENGTH:               20

RAW POST DATA:
{"a":1,"name":"Joe"}

https://echoof.me

```

