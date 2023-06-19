# orm

How do I use Express.js and TypeORM together?
// plain

You can use Express.js and TypeORM together to create a REST API. To do this, you will need to install both Express.js and TypeORM.

To install Express.js, use:
```
npm install express
```

To install TypeORM, use:
```
npm install typeorm
```

Once both packages are installed, you can create a server file that will use Express.js to setup the server and TypeORM to connect to the database.

In the server file, import the necessary packages:
```
const express = require("express");
const typeorm = require("typeorm");
```

Then, create the Express server:
```
const app = express();

app.listen(3000);
console.log("Server started on port 3000");
```

Next, you can configure TypeORM and connect it to the database:
```
typeorm.createConnection({
  type: "postgres",
  host: "localhost",
  port: 5432,
  username: "postgres",
  password: "password",
  database: "testdb",
  synchronize: true,
  logging: false,
  entities: [
    __dirname + "/models/*.js"
  ]
}).then(connection => {
  console.log("Database connection established");
});
```

Finally, you can create your routes and use TypeORM to interact with the database.

For more information on using Express.js and TypeORM together, see [this tutorial](https://typeorm.io/#/tutorials/express-rest-api).

onelinerhub: [orm

How do I use Express.js and TypeORM together?](https://onelinerhub.com/expressjs/orm--how-do-i-use-express-js-and-typeorm-together)