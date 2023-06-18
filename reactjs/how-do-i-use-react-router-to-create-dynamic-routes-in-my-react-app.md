# How do I use React Router to create dynamic routes in my React app?
// plain

React Router is a library used to create dynamic routes in React applications. It allows you to create routes based on the URL path and render components based on the route.

To use React Router, you need to install it as a dependency in your project.

```
npm install react-router-dom
```

Once installed, you can add routes to your application in the `App.js` file.

```js
import { BrowserRouter, Route } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Route exact path="/" component={Home} />
      <Route path="/about" component={About} />
      <Route path="/contact" component={Contact} />
    </BrowserRouter>
  );
}
```

In the example above, we are creating three routes: `/`, `/about`, and `/contact`. Each route will render its respective component when the URL path matches.

The `exact` prop is used to ensure that the `/` route is only rendered when the exact path is matched.

React Router also allows you to pass props to components, create nested routes, and more. For more information, please refer to the [React Router documentation](https://reacttraining.com/react-router/web/guides/quick-start).

onelinerhub: [How do I use React Router to create dynamic routes in my React app?](https://onelinerhub.com/reactjs/how-do-i-use-react-router-to-create-dynamic-routes-in-my-react-app)