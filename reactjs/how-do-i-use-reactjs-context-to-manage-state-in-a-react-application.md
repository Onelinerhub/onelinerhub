# How do I use ReactJS Context to manage state in a React application?
// plain

React Context is a way to pass data through the component tree without having to pass props down manually at every level. It allows you to share a global state between components in a React application.

To use React Context, you need to create a context object with the `React.createContext()` method. Then you need to wrap the components that need to access the context in a `<Context.Provider>` component.

To access the context data, you need to use the `useContext` hook in a functional component or the `static contextType` in a class component.

## Example code

```
import React, { createContext, useContext } from 'react';

// Create a context
const ThemeContext = createContext();

// Create a provider component
function ThemeProvider({ children }) {
  const theme = 'dark';
  return (
    <ThemeContext.Provider value={theme}>
      {children}
    </ThemeContext.Provider>
  );
}

// Create a consumer component
function ThemeConsumer() {
  const theme = useContext(ThemeContext);
  return <h1>Theme is {theme}</h1>;
}
```
## Output example
 `<h1>Theme is dark</h1>`

The code above creates a context object `ThemeContext` and a provider component `ThemeProvider`. The provider component will pass the value `dark` to all the components wrapped in the provider. The consumer component `ThemeConsumer` will access the value `dark` from the context using the `useContext` hook.

## Helpful links
- [React Context Docs](https://reactjs.org/docs/context.html)
- [Using the Context API](https://www.robinwieruch.de/react-context-api)

onelinerhub: [How do I use ReactJS Context to manage state in a React application?](https://onelinerhub.com/reactjs/how-do-i-use-reactjs-context-to-manage-state-in-a-react-application)