# How do I use JSON Web Tokens (JWT) with ReactJS?
// plain

JSON Web Tokens (JWT) are a secure and efficient way to authenticate users in React applications. They can be used to store user identity and authorization information. Here is an example of how to use JWT with ReactJS:

```
// Import JWT library
import jwt from 'jsonwebtoken';

// Create token
const token = jwt.sign({
  userId: 123
}, 'secret');

// Store token in local storage
localStorage.setItem('token', token);

// Retrieve token
const token = localStorage.getItem('token');

// Verify token
const decoded = jwt.verify(token, 'secret');

console.log(decoded); // { userId: 123 }
```

In the example above, we first imported the JWT library. Then, we created a token using the `jwt.sign()` method and stored it in local storage. Finally, we retrieved the token from local storage and used the `jwt.verify()` method to verify the token.

The following are the parts of the example code:

- `jwt.sign()`: This method is used to create a token and takes two parameters: the payload (e.g. userId) and a secret string.
- `localStorage.setItem()`: This method is used to store a token in local storage. It takes two parameters: the key (e.g. 'token') and the value (e.g. the token).
- `localStorage.getItem()`: This method is used to retrieve a token from local storage. It takes one parameter: the key (e.g. 'token').
- `jwt.verify()`: This method is used to verify a token and takes two parameters: the token and a secret string.

For further information on using JWT with React, please refer to the following links:

- [JSON Web Tokens (JWT) with React](https://www.freecodecamp.org/news/json-web-tokens-jwt-with-react/)
- [Using JSON Web Tokens (JWT) with React](https://www.robinwieruch.de/react-jwt-authentication/)

onelinerhub: [How do I use JSON Web Tokens (JWT) with ReactJS?](https://onelinerhub.com/reactjs/how-do-i-use-json-web-tokens--jwt--with-reactjs)