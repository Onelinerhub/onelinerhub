# How do I connect an Express.js application to a MySQL database?
// plain

To connect an Express.js application to a MySQL database, you will need to install the `mysql` module and use it to create a connection.

```javascript
const mysql = require("mysql");

const connection = mysql.createConnection({
  host: "localhost",
  user: "me",
  password: "secret",
  database: "my_db"
});

connection.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
});
```

## Output example

```
Connected!
```

The code above does the following:
1. Require the `mysql` module.
2. Create a connection to the MySQL database using the `createConnection()` method.
3. Connect to the database using the `connect()` method.

You can find more detailed information on connecting to a MySQL database with Express.js in the [Node.js MySQL Documentation](https://github.com/mysqljs/mysql#establishing-connections).

onelinerhub: [How do I connect an Express.js application to a MySQL database?](https://onelinerhub.com/expressjs/how-do-i-connect-an-express-js-application-to-a-mysql-database)