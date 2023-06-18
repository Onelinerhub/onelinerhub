# How do I set up routing in a React.js application?
// plain

To set up routing in a React.js application you need to install the `react-router-dom` package. You can do this by running `npm install react-router-dom` in your terminal.

Once installed, you need to import the `BrowserRouter` component from the `react-router-dom` package and wrap your main `App` component with it.

```javascript
import { BrowserRouter } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      {/* App components here */}
    </BrowserRouter>
  );
}
```

After this, you can create `Route` components inside the `BrowserRouter` component. These `Route` components will take two props: `path` and `component`. The `path` prop will be a string that specifies the path for the route, and the `component` prop will be the component that will be rendered when the route matches.

```javascript
import { BrowserRouter, Route } from 'react-router-dom';
import Home from './Home';
import About from './About';

function App() {
  return (
    <BrowserRouter>
      <Route path="/" exact component={Home} />
      <Route path="/about" component={About} />
    </BrowserRouter>
  );
}
```

Finally, you can use the `Link` component from the `react-router-dom` package to create links that will navigate to the different routes.

```javascript
import { BrowserRouter, Route, Link } from 'react-router-dom';
import Home from './Home';
import About from './About';

function App() {
  return (
    <BrowserRouter>
      <Route path="/" exact component={Home} />
      <Route path="/about" component={About} />

      <Link to="/">Home</Link>
      <Link to="/about">About</Link>
    </BrowserRouter>
  );
}
```

For more information on setting up routing in React, see the [React Router documentation](https://reacttraining.com/react-router/web/guides/quick-start).

onelinerhub: [How do I set up routing in a React.js application?](https://onelinerhub.com/reactjs/how-do-i-set-up-routing-in-a-react-js-application)