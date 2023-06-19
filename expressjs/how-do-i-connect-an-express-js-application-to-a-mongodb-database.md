# How do I connect an Express.js application to a MongoDB database?
// plain

Connecting an Express.js application to a MongoDB database is straightforward and can be done in just a few steps.

1. Install and configure MongoDB and the Mongoose ORM package:

```
npm install mongoose
```

2. Create a connection to the MongoDB database:

```
const mongoose = require('mongoose');
const MONGO_URL = 'mongodb://localhost:27017/myDatabase';
mongoose.connect(MONGO_URL, { useNewUrlParser: true });
```

3. Create a Mongoose schema and model to represent the data in the database:

```
const userSchema = new mongoose.Schema({
  username: String,
  email: String
});
const User = mongoose.model('User', userSchema);
```

4. Use the model to perform CRUD operations on the database:

```
const newUser = new User({
  username: 'John Doe',
  email: 'jdoe@example.com'
});

newUser.save(function(err) {
  if (err) {
    console.log(err);
  } else {
    console.log('User saved successfully!');
  }
});
```

## Output example
 `User saved successfully!`

5. Finally, use the model in your Express.js routes to interact with the database:

```
app.get('/users', function(req, res) {
  User.find({}, function(err, users) {
    if (err) {
      res.send(err);
    } else {
      res.json(users);
    }
  });
});
```

These five steps will allow you to connect an Express.js application to a MongoDB database.

## Helpful links

- [Mongoose Documentation](https://mongoosejs.com/docs/index.html)
- [Express.js Documentation](https://expressjs.com/en/4x/api.html)
- [MongoDB Documentation](https://docs.mongodb.com/)

onelinerhub: [How do I connect an Express.js application to a MongoDB database?](https://onelinerhub.com/expressjs/how-do-i-connect-an-express-js-application-to-a-mongodb-database)