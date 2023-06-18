# How do I implement JWT authentication with ReactJS?
// plain

In order to implement JWT authentication with ReactJS, you need to install the necessary libraries and set up the authentication flow.

1. Install the necessary libraries:
   - [jsonwebtoken](https://www.npmjs.com/package/jsonwebtoken): for generating and verifying JWT tokens
   - [axios](https://www.npmjs.com/package/axios): for making HTTP requests

2. Set up the authentication flow:
   - Create a login component to accept user credentials and make a POST request to the authentication API.
   - On successful authentication, the API will return a JWT token.
   - Store the token in the browser's local storage.
   - For subsequent requests, attach the token in the Authorization header.

## Example code

```javascript
//Login component
import React from 'react';
import axios from 'axios';

const Login = () => {
  const handleLogin = async (e) => {
    e.preventDefault();
    const { email, password } = e.target.elements;
    const response = await axios.post('/auth', {
      email: email.value,
      password: password.value
    });
    const { token } = response.data;
    localStorage.setItem('token', token);
  };
  return (
    <form onSubmit={handleLogin}>
      <input type="text" name="email" />
      <input type="password" name="password" />
      <button type="submit">Login</button>
    </form>
  );
};
export default Login;
```

3. For subsequent requests, attach the token in the Authorization header:

```javascript
const token = localStorage.getItem('token');
const response = await axios.get('/protected-route', {
  headers: {
    Authorization: `Bearer ${token}`
  }
});
```

## Helpful links
- [JSON Web Token (JWT) Tutorial](https://www.toptal.com/web/cookie-free-authentication-with-json-web-tokens-an-example-in-laravel-and-angularjs)
- [Authentication with JWT and React](https://blog.logrocket.com/authentication-with-jwt-and-react/)
- [Authentication in React Apps with JSON Web Tokens](https://daveceddia.com/react-tutorial-jwt-authentication/)

onelinerhub: [How do I implement JWT authentication with ReactJS?](https://onelinerhub.com/reactjs/how-do-i-implement-jwt-authentication-with-reactjs)