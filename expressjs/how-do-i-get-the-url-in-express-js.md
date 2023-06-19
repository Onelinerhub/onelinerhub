# How do I get the URL in Express.js?
// plain

Getting the URL in Express.js is a straightforward process. To do so, you can use the `request` object that is passed to each route handler.

The `request` object has a `url` property that contains the requested URL. The following example demonstrates how to get the URL in Express.js.

```javascript
app.get('/', (req, res) => {
  const url = req.url;
  console.log(url);
  res.send('Hello World');
});
```

The output of the above code block would be the requested URL.

The code consists of:
- `app.get`: This is the Express.js method to create a route handler for a `GET` request.
- `req.url`: This is the `request` object's `url` property that contains the requested URL.
- `console.log`: This is used to log the requested URL to the console.
- `res.send`: This is used to send a response back to the client.

## Helpful links
- [Express.js Request Object Documentation](https://expressjs.com/en/api.html#req)
- [Express.js Response Object Documentation](https://expressjs.com/en/api.html#res)

onelinerhub: [How do I get the URL in Express.js?](https://onelinerhub.com/expressjs/how-do-i-get-the-url-in-express-js)