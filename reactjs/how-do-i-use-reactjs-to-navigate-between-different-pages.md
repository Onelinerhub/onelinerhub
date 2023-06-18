# How do I use ReactJS to navigate between different pages?
// plain

ReactJS is a JavaScript library for building user interfaces. It can be used to create single-page applications which are capable of navigating between different pages. To do this, you need to use React Router.

React Router provides a component called `<Link>` which can be used to navigate to different pages.

```js
import { Link } from 'react-router-dom';

<Link to="/page1">Page 1</Link>
<Link to="/page2">Page 2</Link>
```

This code will render two links, which when clicked will navigate the user to the different pages.

The `<Link>` component takes two props:
1. `to`: The path to the page you want to navigate to.
2. `replace`: A boolean indicating whether to replace the current page in history or push a new page.

React Router also provides other components like `<Route>`, `<Switch>` and `<Redirect>` which can be used to create more complex routing solutions.

## Helpful links
- [React Router Docs](https://reacttraining.com/react-router/web/guides/quick-start)
- [React Router Tutorial](https://www.taniarascia.com/getting-started-with-react-router/)

onelinerhub: [How do I use ReactJS to navigate between different pages?](https://onelinerhub.com/reactjs/how-do-i-use-reactjs-to-navigate-between-different-pages)