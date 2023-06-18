# How can I implement authentication in ReactJS?
// plain

Authentication in ReactJS can be implemented using an authentication library such as [react-router-dom](https://www.npmjs.com/package/react-router-dom) or [react-redux-firebase](https://www.npmjs.com/package/react-redux-firebase).

A basic example of how to implement authentication in ReactJS is provided below:

```javascript
import React from 'react';
import {
  BrowserRouter as Router,
  Route,
  Redirect,
  withRouter
} from 'react-router-dom';

const PrivateRoute = ({ component: Component, ...rest }) => (
  <Route
    {...rest}
    render={props =>
      localStorage.getItem('isAuthenticated') ? (
        <Component {...props} />
      ) : (
        <Redirect
          to={{
            pathname: '/login',
            state: { from: props.location }
          }}
        />
      )
    }
  />
);

export default withRouter(PrivateRoute);
```

This example uses `BrowserRouter` from `react-router-dom` to create a `PrivateRoute` component that checks whether the user is authenticated (by checking `localStorage`) and either renders the requested component or redirects the user to the login page.

## Code explanation


1. `import React from 'react'` - imports the React library
2. `import { BrowserRouter as Router, Route, Redirect, withRouter } from 'react-router-dom'` - imports `BrowserRouter`, `Route`, `Redirect` and `withRouter` components from `react-router-dom`
3. `const PrivateRoute = ({ component: Component, ...rest }) => (` - declares a `PrivateRoute` component that takes in a component as a prop
4. `<Route {...rest} render={props =>` - uses the `Route` component to render the `PrivateRoute` component
5. `localStorage.getItem('isAuthenticated') ? (` - checks if the user is authenticated by checking `localStorage`
6. `<Component {...props} />` - renders the requested component if the user is authenticated
7. `<Redirect to={{ pathname: '/login', state: { from: props.location } }} />` - redirects the user to the login page if the user is not authenticated
8. `export default withRouter(PrivateRoute);` - exports the `PrivateRoute` component

No output is produced by this example code.

onelinerhub: [How can I implement authentication in ReactJS?](https://onelinerhub.com/reactjs/how-can-i-implement-authentication-in-reactjs)