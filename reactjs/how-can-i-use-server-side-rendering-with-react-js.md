# How can I use server-side rendering with React.js?
// plain

Server-side rendering (SSR) with React.js is a popular technique for creating fast and SEO-friendly web applications. It involves rendering the React components on the server before sending them to the browser. This allows the application to be rendered quickly, while also allowing search engines to crawl and index the content.

To use server-side rendering with React.js, you need to use a Node.js server to render the React components. You can use a library such as Next.js or ReactDOMServer to render the components.

## Example code

```
import ReactDOMServer from 'react-dom/server';
import App from './App';

const html = ReactDOMServer.renderToString(<App />);

console.log(html);
```

## Output example

```
<div data-reactroot=""><h1>Hello World</h1></div>
```

The code above is a basic example of server-side rendering with React.js. It imports the ReactDOMServer library and the App component. It then renders the App component to a string and logs the resulting HTML to the console.

## Code explanation


1. `import ReactDOMServer from 'react-dom/server';` - This imports the ReactDOMServer library, which provides the `renderToString()` method for server-side rendering.

2. `import App from './App';` - This imports the App component, which will be rendered on the server.

3. `const html = ReactDOMServer.renderToString(<App />);` - This uses the `renderToString()` method to render the App component and store the resulting HTML in the `html` variable.

4. `console.log(html);` - This logs the HTML to the console.

## Helpful links

- [Next.js](https://nextjs.org/)
- [ReactDOMServer](https://reactjs.org/docs/react-dom-server.html)

onelinerhub: [How can I use server-side rendering with React.js?](https://onelinerhub.com/reactjs/how-can-i-use-server-side-rendering-with-react-js)