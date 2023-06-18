# How do I use SQLite with npm?
// plain

**Using SQLite with npm**

SQLite can be used with npm by installing the `sqlite3` npm package. This package provides an asynchronous, non-blocking SQLite3 bindings for Node.js.

To install the package, run the following command:
```
npm install sqlite3
```

Once the package is installed, you can use it in your Node.js application. The following example code demonstrates how to create a database and run a simple query:

```javascript
// create a database
const sqlite3 = require('sqlite3');
const db = new sqlite3.Database('example.db');

// run a query
db.run("CREATE TABLE IF NOT EXISTS people (name TEXT, age INTEGER)");
db.run("INSERT INTO people (name, age) VALUES ('John', 25)");

// get the results
db.all("SELECT * FROM people", (err, rows) => {
  console.log(rows);
});
```

The output of this code will be:
```
[ { name: 'John', age: 25 } ]
```

The code consists of the following parts:
- `sqlite3`: the npm package
- `db`: the database object
- `db.run`: the method to run a query
- `db.all`: the method to get the results of a query

For more information, see the [sqlite3 npm package documentation](https://www.npmjs.com/package/sqlite3).

onelinerhub: [How do I use SQLite with npm?](https://onelinerhub.com/sqlite/how-do-i-use-sqlite-with-npm)