# How can I use TypeScript with React.js to define an onClick event?
// plain

In order to use TypeScript with React.js to define an onClick event, you need to first create a React component and then define the onClick event as a function inside the component. The function should have an event parameter of type React.MouseEvent.

```
import React, { MouseEvent } from 'react';

interface Props {
  onClick: (e: MouseEvent) => void;
}

const MyComponent: React.FC<Props> = ({ onClick }) => {
  return <button onClick={onClick}>Click me!</button>;
};

export default MyComponent;
```

The onClick function can then be passed to the React component as a prop.

```
import React from 'react';
import MyComponent from './MyComponent';

const App = () => {
  const handleClick = (e: React.MouseEvent) => {
    console.log('Button was clicked!');
  };

  return <MyComponent onClick={handleClick} />;
};

export default App;
```

The output of this example code will be a button that when clicked, will log "Button was clicked!" to the console.

## Code explanation


1. `import React, { MouseEvent } from 'react';` - This imports the React library and the MouseEvent type from the React library.

2. `interface Props { onClick: (e: MouseEvent) => void; }` - This defines the props for the React component, with the onClick prop being a function that takes a MouseEvent parameter and returns nothing.

3. `const MyComponent: React.FC<Props> = ({ onClick }) => {...}` - This is the React component that takes the onClick prop as a parameter and renders a button that calls the onClick function when clicked.

4. `const handleClick = (e: React.MouseEvent) => {...}` - This is the function that will be called when the button is clicked.

5. `return <MyComponent onClick={handleClick} />` - This passes the handleClick function as a prop to the MyComponent component.

## Helpful links

- [TypeScript React Tutorial](https://www.typescriptlang.org/docs/handbook/react-&-webpack.html)
- [React MouseEvent](https://reactjs.org/docs/events.html#mouse-events)

onelinerhub: [How can I use TypeScript with React.js to define an onClick event?](https://onelinerhub.com/reactjs/how-can-i-use-typescript-with-react-js-to-define-an-onclick-event)