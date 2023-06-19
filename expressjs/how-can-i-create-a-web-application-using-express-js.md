# How can I create a web application using Express.js?
// plain

Creating a web application using Express.js is a straightforward process.

1. Install Express.js by running `npm install express`
2. Create a JavaScript file, for example `app.js`
3. Require Express.js in the file with `const express = require('express')`
4. Create an Express.js application by running `const app = express()`
5. Define routes for the application with `app.get()` and `app.post()`
6. Start the server with `app.listen()`
7. Test the application by visiting the URL specified in `app.listen()`

## Example code

```
const express = require('express')
const app = express()

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(3000, () => {
  console.log('Server started on port 3000')
})
```

## Output example

```
Server started on port 3000
```

## Helpful links
- [Express.js Documentation](https://expressjs.com/en/4x/api.html)
- [Getting Started with Express.js](https://expressjs.com/en/starter/hello-world.html)

onelinerhub: [How can I create a web application using Express.js?](https://onelinerhub.com/expressjs/how-can-i-create-a-web-application-using-express-js)