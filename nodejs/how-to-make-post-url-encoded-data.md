# How to post url-encoded data

```js
const https = require('https');
const qs = require('querystring');

let data = {name: 'Joe', age: 98};
let body = qs.stringify(data);

let req = https.request({
  hostname: 'echoof.me',
  port: 443,
  path: '/',
  method: 'POST',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': body.length
  }
}, (resp) => {
  let data = '';
  resp.on('data', (chunk) => { data += chunk; });

  resp.on('end', () => {
    console.log(data);
  });
});

req.write(body);
```

- `require('https')` - standard library to do `HTTP` requests
- `require('querystring')` - lib to manage query strings
- `{name: 'Joe', age: 98}` - sample data to post
- `qs.stringify(` - convert given object to query string
- `application/x-www-form-urlencoded` - let Nodejs know we are going to send url-encoded query string 
- `req.write(body)` - write encoded data to request (sends encoded post data to server)

group: http_request

## Example: 
```js
const https = require('https');
const qs = require('querystring');

let data = {name: 'Joe', age: 98};
let body = qs.stringify(data);

let req = https.request({
  hostname: 'echoof.me',
  port: 443,
  path: '/',
  method: 'POST',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': body.length
  }
}, (resp) => {
  let data = '';
  resp.on('data', (chunk) => { data += chunk; });

  resp.on('end', () => {
    console.log(data);
  });
});

req.write(body);
```
```
IP:                           135.181.98.214

CONNECTION:                   close
CONTENT_LENGTH:               15
CONTENT_TYPE:                 application/x-www-form-urlencoded

DATA name:                    Joe
DATA age:                     98

https://echoof.me

```

