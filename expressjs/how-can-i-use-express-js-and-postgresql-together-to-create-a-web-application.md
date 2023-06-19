# How can I use Express.js and PostgreSQL together to create a web application?
// plain

Express.js and PostgreSQL can be used together to create a web application.

## Example code

```
const express = require('express')
const { Client } = require('pg')

const app = express()

const client = new Client({
  user: 'postgres',
  host: 'localhost',
  database: 'my_database',
  password: 'my_password',
  port: 5432,
})

client.connect()

app.get('/', (req, res) => {
  client.query('SELECT * FROM users', (err, result) => {
    if (err) {
      console.log(err.stack)
    } else {
      res.send(result.rows)
    }
  })
})

app.listen(3000, () => {
  console.log('Server listening on port 3000')
})
```

## Output example

```
Server listening on port 3000
```

This code creates an Express.js application which connects to a PostgreSQL database and sends a query to the users table. It then sends the result of the query to the client.

## Code explanation


1. `const express = require('express')`: This imports the Express.js module.
2. `const { Client } = require('pg')`: This imports the PostgreSQL Client module.
3. `const app = express()`: This creates an Express.js application.
4. `const client = new Client({...})`: This creates a new PostgreSQL Client instance with the given configuration.
5. `client.connect()`: This connects to the PostgreSQL database.
6. `app.get('/', (req, res) => {...})`: This creates a route handler for the root route which sends a query to the users table in the database and sends the result to the client.
7. `app.listen(3000, () => {...})`: This starts the Express.js application on port 3000.

## Helpful links

- [Express.js](https://expressjs.com/)
- [PostgreSQL](https://www.postgresql.org/)

onelinerhub: [How can I use Express.js and PostgreSQL together to create a web application?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-and-postgresql-together-to-create-a-web-application)