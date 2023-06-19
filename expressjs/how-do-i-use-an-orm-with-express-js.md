# How do I use an ORM with Express.js?
// plain

An ORM (Object Relational Mapping) is a library that simplifies database interactions for Express.js applications. ORMs allow developers to write code that interacts with a database without having to write SQL queries.

To use an ORM with Express.js, you will need to install the ORM library and configure it to connect to your database. For example, to use Sequelize with Express.js, you would install the library with `npm install sequelize` and then configure it to connect to your database with:

```javascript
const Sequelize = require('sequelize');
const sequelize = new Sequelize('database', 'username', 'password', {
  host: 'localhost',
  dialect: 'mysql'
});
```

Once the ORM is connected to the database, you can use it in your Express.js application. For example, to create a new record in the database with Sequelize, you would use the `create` method:

```javascript
const User = sequelize.define('user', {
  firstName: Sequelize.STRING,
  lastName: Sequelize.STRING
});

User.create({
  firstName: 'John',
  lastName: 'Doe'
}).then(user => {
  console.log(user.get({
    plain: true
  }));
});
```

The output of the above code would be:
```
{ firstName: 'John', lastName: 'Doe', id: 1 }
```

ORMs are a powerful tool for Express.js applications and can greatly simplify database interactions. For more information, see the [Sequelize documentation](https://sequelize.org/v5/manual/getting-started.html) or the [Mongoose documentation](https://mongoosejs.com/docs/index.html).

onelinerhub: [How do I use an ORM with Express.js?](https://onelinerhub.com/expressjs/how-do-i-use-an-orm-with-express-js)