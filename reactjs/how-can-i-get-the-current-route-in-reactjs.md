# How can I get the current route in ReactJS?
// plain

In order to get the current route in ReactJS, you can use the `useLocation` hook from the `react-router-dom` package.

```
import { useLocation } from 'react-router-dom';

const MyComponent = () => {
  const { pathname } = useLocation();

  console.log(pathname);
}

// Output: '/about'
```

The `useLocation` hook returns an object with the following properties:

- `pathname`: The path of the current location (e.g. `/about`).
- `search`: The query string of the current location (e.g. `?foo=bar`).
- `hash`: The hash of the current location (e.g. `#foo`).
- `state`: The state of the current location (e.g. `{ foo: 'bar' }`).

It is also possible to get the current route using the `withRouter` higher-order component from `react-router-dom`:

```
import { withRouter } from 'react-router-dom';

const MyComponent = ({ location }) => {
  console.log(location.pathname);
}

export default withRouter(MyComponent);

// Output: '/about'
```

The `withRouter` higher-order component passes the `location` object as a prop to the wrapped component.

## Helpful links

- [React Router - useLocation Hook](https://reactrouter.com/web/api/Hooks/uselocation)
- [React Router - withRouter Higher-Order Component](https://reactrouter.com/web/api/withRouter)

onelinerhub: [How can I get the current route in ReactJS?](https://onelinerhub.com/reactjs/how-can-i-get-the-current-route-in-reactjs)