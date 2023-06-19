# How can I use dotenv with ExpressJS?
// plain

Using dotenv with ExpressJS is a great way to store environment variables in a secure manner. Environment variables are typically used to store sensitive information such as API keys and passwords, and dotenv provides a secure way of storing and retrieving them.

To use dotenv with ExpressJS, first install the dotenv package:

```
npm install dotenv
```

Next, create a `.env` file in the root of your project and add your environment variables to it. For example:

```
DB_USERNAME=myusername
DB_PASSWORD=mypassword
```

Now, in your ExpressJS application, you can require the dotenv package and call the `config()` method to load the environment variables from the `.env` file.

```javascript
require('dotenv').config();
```

You can then access the environment variables using `process.env`, for example:

```javascript
console.log(process.env.DB_USERNAME);
// Output: myusername
```

For more information on using dotenv with ExpressJS, see [this article](https://medium.com/@thejasonfile/using-dotenv-package-to-create-environment-variables-33da4ac4ea8f).

onelinerhub: [How can I use dotenv with ExpressJS?](https://onelinerhub.com/expressjs/how-can-i-use-dotenv-with-expressjs)