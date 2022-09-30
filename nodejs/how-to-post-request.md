# How to make GET request

```js
const https = require('https');

https.get('https://echoof.me/', (resp) => {
  let data = '';
  resp.on('data', (chunk) => { data += chunk; });

  resp.on('end', () => {
    console.log(data);
  });
})
```

- `require('https')` - standard library to do `HTTP` requests
- `https.get` - make `GET` request to the given URL
- `resp.on('data'` - handle response in chunks
- `(chunk) => { data += chunk; }` - collect all response chunks into single string
- `resp.on('end'` - fired when response ended
- `console.log(data);` - outputs full response from given URL

group: http_request

## Example: 
```js
const https = require('https');

https.get('https://echoof.me/', (resp) => {
  let data = '';
  resp.on('data', (chunk) => { data += chunk; });

  resp.on('end', () => {
    console.log(data);
  });
})
```
```
IP:                           135.181.98.214

CONNECTION:                   close

https://echoof.me

```

link_youtube: https://youtu.be/vKGp3X3Otf8
