# How can I use Express.js to create a redirect?
// plain

Express.js is a web application framework for Node.js that allows you to create a web server and route requests. You can use Express.js to create a redirect by using the `res.redirect()` function. This function takes two parameters, the first is the destination URL and the second is an optional status code.

## Example code

```
app.get('/', (req, res) => {
    res.redirect('/home')
})
```

This code creates a redirect from the root route `/` to `/home`.

The code consists of:

1. `app.get('/', (req, res) => {` - This is the route handler for the root route `/`.
2. `res.redirect('/home')` - This is the `res.redirect()` function which takes the destination URL as a parameter and creates a redirect.

## Helpful links
- [Express.js Documentation](https://expressjs.com/en/api.html#res.redirect)

onelinerhub: [How can I use Express.js to create a redirect?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-to-create-a-redirect)