# How to do a POST request

```javascript
fetch('https://example.org/script', {
  method: 'post',
  body: 'a=1'
}).then(function(r) {
  return r.json();
}).then(function(data) {
  console.log(data);
});
```

- `fetch(` - sends request to specified URL and reads response
- `example.org/script` - let's post something to this URL
- `method: 'post'` - we want to send POST request
- `body:` - POST request body
- `r.json()` - we assume our backend responds with JSON
- `console.log(data)` - do something with response data


link_youtube: https://youtu.be/vMif8cQJNEA
