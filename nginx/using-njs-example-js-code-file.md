# Using NJs example (JS code file)

```js
function test(r) {
  r.return(200, "Hi everyone");
}

export default {test}
```

- `test()` - sample function that is [called from Nginx](/nginx/using-njs-example)
- `r.return` - returns HTTP response
- `200` - HTTP status code
- `Hi everyone` - sample body to return
- `export default` - list what we want to use in Nginx

group: njs


