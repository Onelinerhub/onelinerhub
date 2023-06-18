# How do I use the React useState hook?
// plain

The React `useState` hook is a built-in hook that allows a component to have a state. It is a way to manage and update the component's state without using a class component.

## Example code

```
import React, { useState } from 'react';

const Example = () => {
  // Declare a new state variable, which we'll call "count"
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
}
```

In the example, the `useState` hook is used to declare a new state variable called `count` which is set to 0. The `setCount` function is used to update the state variable when the button is clicked.

## Code explanation

* `import React, { useState } from 'react';` - imports the `useState` hook from the React library
* `const [count, setCount] = useState(0);` - declares a new state variable called `count` and sets it to 0
* `<button onClick={() => setCount(count + 1)}>` - adds an `onClick` event handler to the button which calls the `setCount` function to update the `count` state variable

## Helpful links
* [React useState Hook Documentation](https://reactjs.org/docs/hooks-state.html)
* [useState Explained](https://www.robinwieruch.de/react-state-use-state/)

onelinerhub: [How do I use the React useState hook?](https://onelinerhub.com/reactjs/how-do-i-use-the-react-usestate-hook)