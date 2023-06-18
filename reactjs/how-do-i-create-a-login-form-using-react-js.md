# How do I create a login form using React.js?
// plain

Creating a login form with React.js is a straightforward process. Here is an example of a simple login form that takes in a username and a password:

```
import React, { useState } from 'react';

const LoginForm = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(`Username: ${username}`);
    console.log(`Password: ${password}`);
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Username
        <input
          type="text"
          value={username}
          onChange={e => setUsername(e.target.value)}
        />
      </label>
      <label>
        Password
        <input
          type="password"
          value={password}
          onChange={e => setPassword(e.target.value)}
        />
      </label>
      <input type="submit" value="Submit" />
    </form>
  );
};

export default LoginForm;
```

The code above will render the following form:

Username: ___________
Password: ___________
Submit

The code is composed of several parts:

- The imports: `import React, { useState } from 'react';` imports the React library and the `useState` hook from React, which is necessary for creating and updating state in React components.

- The `LoginForm` component: this is the main component that renders the login form.

- The `handleSubmit` function: this function is called when the form is submitted and handles the logic for processing the username and password.

- The `input` elements: these elements render the form fields and update the `username` and `password` state variables when they change.

- The `submit` button: this is the button that submits the form, which calls the `handleSubmit` function.

## Helpful links

- [React documentation for forms](https://reactjs.org/docs/forms.html)
- [React hooks documentation](https://reactjs.org/docs/hooks-intro.html)

onelinerhub: [How do I create a login form using React.js?](https://onelinerhub.com/reactjs/how-do-i-create-a-login-form-using-react-js)