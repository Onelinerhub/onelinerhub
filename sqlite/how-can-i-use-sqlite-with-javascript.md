# How can I use SQLite with JavaScript?
// plain

SQLite is a lightweight database that can be used with JavaScript. It is a self-contained, serverless, zero-configuration, and transactional SQL database engine. It can be used to store and retrieve data in a structured format.

To use SQLite with JavaScript, you need to install the sqlite3 package. This can be done using the following command:

```
npm install sqlite3
```

Once the package is installed, you can create a connection to the database using the following code:

```
const sqlite3 = require('sqlite3');
const db = new sqlite3.Database('./database.db');
```

You can then use the `db` object to execute SQL queries. For example, to create a table, you can use the following code:

```
db.run('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)');
```

To insert data into the table, you can use the following code:

```
db.run('INSERT INTO users(name, age) VALUES (?, ?)', ['John', 21]);
```

Finally, to retrieve data from the table, you can use the following code:

```
db.all('SELECT * FROM users', (err, rows) => {
  console.log(rows);
});
```

## Output example

```
[ { id: 1, name: 'John', age: 21 } ]
```

- `npm install sqlite3`: Installs the sqlite3 package.
- `const sqlite3 = require('sqlite3');`: Imports the sqlite3 package.
- `const db = new sqlite3.Database('./database.db');`: Creates a connection to the database.
- `db.run('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)');`: Creates a table.
- `db.run('INSERT INTO users(name, age) VALUES (?, ?)', ['John', 21]);`: Inserts data into the table.
- `db.all('SELECT * FROM users', (err, rows) => { console.log(rows); });`: Retrieves data from the table.

## Helpful links
- [SQLite](https://www.sqlite.org/)
- [sqlite3 npm package](https://www.npmjs.com/package/sqlite3)

onelinerhub: [How can I use SQLite with JavaScript?](https://onelinerhub.com/sqlite/how-can-i-use-sqlite-with-javascript)