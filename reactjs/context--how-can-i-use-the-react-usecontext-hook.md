# Context

How can I use the React useContext hook?
// plain

The React `useContext` hook is used to access data that is provided by a Context object. It allows components to subscribe to a Context object without having to pass the data down through multiple levels of the component tree.

## Example code


```
import React, { useContext } from 'react';

const MyContext = React.createContext();

function App() {
  const value = useContext(MyContext);
  return <div>{value}</div>;
}
```

## Output example


```
<div>{value}</div>
```

In the above example, the `useContext` hook is used to access the value of the `MyContext` object. The value of `MyContext` is then rendered in the `<div>` element.

The `useContext` hook can also be used to update the value of the `MyContext` object. For example:

```
import React, { useContext, useState } from 'react';

const MyContext = React.createContext();

function App() {
  const [value, setValue] = useState('');
  const contextValue = useContext(MyContext);
  setValue(contextValue);
  return <div>{value}</div>;
}
```

## Output example


```
<div>{value}</div>
```

In the above example, the `useContext` hook is used to access the value of the `MyContext` object, and the `useState` hook is used to update the value of `MyContext`. The updated value of `MyContext` is then rendered in the `<div>` element.

## Helpful links

- [React useContext Hook Documentation](https://reactjs.org/docs/hooks-reference.html#usecontext)
- [React Context API Documentation](https://reactjs.org/docs/context.html)

onelinerhub: [Context

How can I use the React useContext hook?](https://onelinerhub.com/reactjs/context--how-can-i-use-the-react-usecontext-hook)