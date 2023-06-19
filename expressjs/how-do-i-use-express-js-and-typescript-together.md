# How do I use Express.js and TypeScript together?
// plain

Using Express.js and TypeScript together is a great way to create powerful and robust web applications. Here's an example of how to do it:

```
// app.ts
import express from 'express';

// Create an Express app
const app = express();

// Add middleware
app.use(express.json());

// Add routes
app.get('/', (req, res) => {
    res.send('Hello World!');
});

// Start the server
app.listen(3000, () => console.log('Server running on port 3000'));
```

## Output example

```
Server running on port 3000
```

1. Import the express module `import express from 'express';`
2. Create an Express app `const app = express();`
3. Add middleware to the app `app.use(express.json());`
4. Add routes to the app `app.get('/', (req, res) => { res.send('Hello World!'); });`
5. Start the server `app.listen(3000, () => console.log('Server running on port 3000'));`

## Helpful links

- [Express.js](https://expressjs.com/)
- [TypeScript](https://www.typescriptlang.org/)

onelinerhub: [How do I use Express.js and TypeScript together?](https://onelinerhub.com/expressjs/how-do-i-use-express-js-and-typescript-together)