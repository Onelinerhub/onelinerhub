# How do I use Express.js to get a user's IP address?
// plain

Using Express.js to get a user's IP address is very simple. The following example will show how to do this:

```
const express = require('express')
const app = express()

app.get('/', (req, res) => {
    const ip = req.ip
    console.log(ip)
    res.send(ip)
})

app.listen(3000, () => console.log('Listening on port 3000'))
```

In the example above, the `req` object is used to get the user's IP address. The `req.ip` property returns the user's IP address as a string. The IP address is then printed out to the console and sent as a response to the user.

## Code explanation


- `const express = require('express')`: imports the Express.js module.
- `const app = express()`: creates an instance of the Express.js application.
- `app.get('/', (req, res) => { ... })`: defines a route handler for the `GET` request to the `/` route.
- `const ip = req.ip`: gets the user's IP address from the `req` object.
- `console.log(ip)`: prints the IP address to the console.
- `res.send(ip)`: sends the IP address as a response to the user.
- `app.listen(3000, () => console.log('Listening on port 3000'))`: starts the Express.js server on port 3000.

The output of the example code will be the user's IP address printed out to the console.

## Helpful links

- [Express.js Documentation](https://expressjs.com/en/4x/api.html)
- [Express.js Request Object Documentation](https://expressjs.com/en/4x/api.html#req)

onelinerhub: [How do I use Express.js to get a user's IP address?](https://onelinerhub.com/expressjs/how-do-i-use-express-js-to-get-a-user-s-ip-address)