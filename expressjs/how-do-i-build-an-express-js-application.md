# How do I build an Express.js application?
// plain

An Express.js application can be built by following the steps below:

1. Install the Express.js framework:
```
npm install express
```

2. Create an application object:
```javascript
const express = require('express');
const app = express();
```

3. Set up routes:
```javascript
app.get('/', (req, res) => {
    res.send('Hello World');
});
```

4. Set up a server:
```javascript
const port = 3000;

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
```

5. Output:
```
Server running on port 3000
```

6. Test the application:
Open a web browser and navigate to http://localhost:3000.

7. ## Helpful links
- [Express.js Getting Started Guide](https://expressjs.com/en/starter/installing.html)
- [Express.js Routing Guide](https://expressjs.com/en/guide/routing.html)

onelinerhub: [How do I build an Express.js application?](https://onelinerhub.com/expressjs/how-do-i-build-an-express-js-application)