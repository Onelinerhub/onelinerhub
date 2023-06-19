# How can I create a quiz using Express.js?
// plain

Creating a quiz using Express.js is a great way to add interactivity to a website. Here is an example of how to create a simple quiz using Express.js:

```
// Require Express
const express = require('express');

// Create an Express application
const app = express();

// Set a route for the quiz
app.get('/quiz', (req, res) => {
  // Render the quiz page
  res.render('quiz');
});

// Set a route for the quiz results
app.post('/quiz-results', (req, res) => {
  // Get the user's answers
  const userAnswers = req.body;

  // Calculate the user's score
  let score = 0;
  // Loop through the user's answers and increment the score
  // for each correct answer
  for (let answer of userAnswers) {
    if (answer === 'correct') {
      score++;
    }
  }

  // Render the results page
  res.render('quiz-results', {score});
});

// Start the server
app.listen(3000);
```

This example code creates an Express application with two routes. The first route `/quiz` renders the quiz page and the second route `/quiz-results` calculates the user's score and renders the results page.

## Code explanation


1. Require Express: `const express = require('express');`
2. Create an Express application: `const app = express();`
3. Set a route for the quiz: `app.get('/quiz', (req, res) => { ... });`
4. Set a route for the quiz results: `app.post('/quiz-results', (req, res) => { ... });`
5. Get the user's answers: `const userAnswers = req.body;`
6. Calculate the user's score: `let score = 0; for (let answer of userAnswers) { ... }`
7. Render the results page: `res.render('quiz-results', {score});`
8. Start the server: `app.listen(3000);`

## Helpful links

- [Express.js Documentation](https://expressjs.com/en/4x/api.html)
- [Node.js Documentation](https://nodejs.org/api/http.html)

onelinerhub: [How can I create a quiz using Express.js?](https://onelinerhub.com/expressjs/how-can-i-create-a-quiz-using-express-js)