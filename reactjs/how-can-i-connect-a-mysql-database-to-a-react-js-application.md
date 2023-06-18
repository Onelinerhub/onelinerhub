# How can I connect a MySQL database to a React.js application?
// plain

Connecting a MySQL database to a React.js application is relatively simple.

First, you must install the necessary packages to connect the two. This can be done by running the following command in your terminal:
```
npm install mysql
```

Once the packages are installed, you can connect to the database by creating a connection object in your React code. This can be done with the following code:

```
let connection = mysql.createConnection({
  host: 'localhost',
  user: 'user',
  password: 'password',
  database: 'database'
});
```

Once the connection object is created, you can then establish the connection to the database. This can be done with the following code:

```
connection.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
});
```

Once the connection is established, you can then execute queries on the database. This can be done with the following code:

```
connection.query('SELECT * FROM table', function (err, rows) {
  if (err) throw err;
  console.log('Data received from Db:\n');
  console.log(rows);
});
```

Once the query is executed, you can then close the connection. This can be done with the following code:

```
connection.end(function(err) {
  // The connection is terminated now
});
```

## Helpful links
- [MySQL NPM package](https://www.npmjs.com/package/mysql)
- [MySQL Node.js tutorial](https://www.w3schools.com/nodejs/nodejs_mysql.asp)

onelinerhub: [How can I connect a MySQL database to a React.js application?](https://onelinerhub.com/reactjs/how-can-i-connect-a-mysql-database-to-a-react-js-application)