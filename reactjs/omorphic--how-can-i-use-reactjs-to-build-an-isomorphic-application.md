# omorphic

How can I use ReactJS to build an isomorphic application?
// plain

Isomorphic applications are web applications that are able to run both on the server and the client. ReactJS can be used to build an isomorphic application by leveraging its server-side rendering capabilities. To do this, first create a React component that renders on the server-side:

```
import React from 'react';

class App extends React.Component {
  render() {
    return <h1>Hello, world!</h1>;
  }
}

export default App;
```

This component can then be rendered on the server-side using ReactDOMServer:

```
import React from 'react';
import ReactDOMServer from 'react-dom/server';
import App from './App';

const html = ReactDOMServer.renderToString(<App />);
console.log(html); // <h1 data-reactroot="">Hello, world!</h1>
```

The rendered HTML can then be sent to the client, where the same React component can be used to render the application on the client-side:

```
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

const root = document.getElementById('root');
ReactDOM.render(<App />, root);
```

This approach allows for code reuse between the server and the client, resulting in an isomorphic application.

Parts of the code:

1. `import React from 'react';` - This imports the React library.
2. `class App extends React.Component {` - This creates a React component class.
3. `render() {` - This is the method used to render the component.
4. `ReactDOMServer.renderToString(<App />);` - This renders the component on the server-side.
5. `ReactDOM.render(<App />, root);` - This renders the component on the client-side.

## Helpful links

- [React Documentation - Server Rendering](https://reactjs.org/docs/react-dom-server.html)
- [React Documentation - ReactDOM](https://reactjs.org/docs/react-dom.html)

onelinerhub: [omorphic

How can I use ReactJS to build an isomorphic application?](https://onelinerhub.com/reactjs/omorphic--how-can-i-use-reactjs-to-build-an-isomorphic-application)