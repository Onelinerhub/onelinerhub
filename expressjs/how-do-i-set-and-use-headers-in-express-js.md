# How do I set and use headers in Express.js?
// plain

To set and use headers in Express.js, you can use the `app.use()` and `res.header()` methods.

The `app.use()` method is used to set the headers for all requests and responses. For example, the following code sets the `Content-Type` header to `application/json` for all requests and responses:

```javascript
app.use(function (req, res, next) {
    res.header("Content-Type", "application/json");
    next();
});
```

The `res.header()` method is used to set the headers for a specific request and response. For example, the following code sets the `Content-Type` header to `application/json` for a specific response:

```javascript
app.get("/", function (req, res) {
    res.header("Content-Type", "application/json");
    res.send({"message": "Hello World!"});
});
```

## Output example

```
{"message": "Hello World!"}
```

The `req.header()` method is used to get the headers for a specific request. For example, the following code gets the `Content-Type` header for a specific request:

```javascript
app.get("/", function (req, res) {
    let contentType = req.header("Content-Type");
    console.log(contentType);
});
```

## Output example

```
application/json
```

## Helpful links
- [Express.js Documentation](https://expressjs.com/en/4x/api.html)
- [MDN Web Docs - HTTP Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)

onelinerhub: [How do I set and use headers in Express.js?](https://onelinerhub.com/expressjs/how-do-i-set-and-use-headers-in-express-js)