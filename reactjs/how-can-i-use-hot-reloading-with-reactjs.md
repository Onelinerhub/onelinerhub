# How can I use hot reloading with ReactJS?
// plain

Hot reloading is a feature of ReactJS that allows developers to make changes to the code and see the results immediately in the browser without having to reload the page. It is a great way to quickly test and debug components.

To use hot reloading with ReactJS, you will need to install the react-hot-loader package. This package allows for hot reloading of React components.

Once the package is installed, the following code can be used to enable hot reloading in a React app:

```
import { hot } from 'react-hot-loader/root';

const App = () => {
  return <div>Hello World!</div>;
};

export default hot(App);
```

The `hot` function from the `react-hot-loader/root` package wraps the App component and enables hot reloading. Any changes made to the App component will be reflected in the browser without having to reload the page.

For more information on using hot reloading with ReactJS, see the following links:

- [React Hot Loader Documentation](https://github.com/gaearon/react-hot-loader)
- [React Hot Loader Tutorial](https://www.robinwieruch.de/react-hot-loader)

onelinerhub: [How can I use hot reloading with ReactJS?](https://onelinerhub.com/reactjs/how-can-i-use-hot-reloading-with-reactjs)