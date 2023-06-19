# How do I use Express.js to process form data?
// plain

Express.js is a web application framework for Node.js designed to make building web applications easier. It can be used to process form data in the following way:

1. Create a form in HTML and add an action attribute to the form element which points to the route that will handle the form submission.

```
<form action="/form-submission" method="POST">
  <input type="text" name="name" />
  <input type="submit" value="Submit" />
</form>
```

2. Create a route to handle the form submission.

```
app.post('/form-submission', (req, res) => {
  const name = req.body.name;
  res.send(`Hello ${name}`);
});
```

3. When the form is submitted, the `req.body` object will contain the data from the form.

## Output example
 `Hello <name>`

4. Finally, you can use the data from the form in your application.

## Helpful links
- [Express.js](https://expressjs.com/)
- [Node.js](https://nodejs.org/)
- [Forms in HTML](https://www.w3schools.com/html/html_forms.asp)

onelinerhub: [How do I use Express.js to process form data?](https://onelinerhub.com/expressjs/how-do-i-use-express-js-to-process-form-data)