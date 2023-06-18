# How can I use SQLite with Node.js?
// plain

SQLite is a popular, open-source, lightweight relational database system. It is often used with Node.js due to its simple setup and ease of use. To use SQLite with Node.js, you must first install the sqlite3 module.

```
$ npm install sqlite3
```

Once the module is installed, you can create a database connection and perform SQL queries. The following example code creates a database connection and executes a query to create a table.

```
const sqlite3 = require('sqlite3').verbose();

let db = new sqlite3.Database(':memory:', (err) => {
  if (err) {
    return console.error(err.message);
  }
  console.log('Connected to the in-memory SQlite database.');
});

db.run('CREATE TABLE test_table (name TEXT)', (err) => {
  if (err) {
    return console.error(err.message);
  }
  console.log('Table created successfully.');
});
```

## Output example

```
Connected to the in-memory SQlite database.
Table created successfully.
```

The code above:

1. Imports the `sqlite3` module (`const sqlite3 = require('sqlite3').verbose();`)
2. Creates a database connection (`let db = new sqlite3.Database(':memory:', (err) => {`)
3. Executes a query to create a table (`db.run('CREATE TABLE test_table (name TEXT)', (err) => {`)

For more information, see the [sqlite3 documentation](https://www.npmjs.com/package/sqlite3) and the [Node.js documentation](https://nodejs.org/api/sqlite3.html).

onelinerhub: [How can I use SQLite with Node.js?](https://onelinerhub.com/sqlite/how-can-i-use-sqlite-with-node-js)