# How do I render a template using Express.js?
// plain

To render a template using Express.js, you need to set up a view engine such as Pug or EJS. After you have done that, you can use `res.render()` to render a template.

```javascript
// Example
app.get('/', function (req, res) {
  res.render('index', { title: 'My App' });
});
```

This will render the `index` template with the `title` variable set to `My App`.

## Code explanation

- `app.get()`: Used to set up a route for the application
- `res.render()`: Used to render a template with the given parameters

## Helpful links
- [Express.js Documentation](https://expressjs.com/en/4x/api.html#res.render)
- [Pug Documentation](https://pugjs.org/api/getting-started.html)
- [EJS Documentation](https://ejs.co/#docs)

onelinerhub: [How do I render a template using Express.js?](https://onelinerhub.com/expressjs/how-do-i-render-a-template-using-express-js)