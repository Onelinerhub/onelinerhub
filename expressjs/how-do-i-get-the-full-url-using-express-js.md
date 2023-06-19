# How do I get the full URL using Express.js?
// plain

To get the full URL using Express.js, you can use the `req.protocol`, `req.get('host')` and `req.originalUrl` properties.

## Example code

```
const fullUrl = req.protocol + '://' + req.get('host') + req.originalUrl;
console.log(fullUrl);
```

## Output example

```
https://example.com/users/1
```

The code above uses the following properties:

* `req.protocol` - the request protocol, usually either http or https
* `req.get('host')` - the hostname of the request
* `req.originalUrl` - the original request URL

## Helpful links

* [Express.js Request Object Documentation](https://expressjs.com/en/api.html#req)

onelinerhub: [How do I get the full URL using Express.js?](https://onelinerhub.com/expressjs/how-do-i-get-the-full-url-using-express-js)