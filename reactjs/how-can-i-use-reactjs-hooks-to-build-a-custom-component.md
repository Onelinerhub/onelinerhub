# How can I use ReactJS Hooks to build a custom component?
// plain

ReactJS Hooks are a powerful tool for building custom components. Hooks allow you to use state and other React features without writing a class. To use ReactJS Hooks to build a custom component, you can use the useState() hook to declare a state variable, and the useEffect() hook to update the state variable. Here is an example of how to build a custom component with ReactJS Hooks:

```
import React, { useState, useEffect } from 'react';

const MyCustomComponent = () => {
  const [myState, setMyState] = useState(0);

  useEffect(() => {
    setMyState(myState + 1);
  }, [myState]);

  return (
    <div>
      <p>My state is {myState}</p>
    </div>
  );
};

export default MyCustomComponent;
```

This example will render a component that displays the value of the `myState` variable, which is initially set to 0, and increases by 1 each time the component is rendered.

The code consists of the following parts:

1. `import React, { useState, useEffect } from 'react';` - This imports the `useState` and `useEffect` hooks from the React library.
2. `const [myState, setMyState] = useState(0);` - This declares a state variable called `myState` and assigns it an initial value of 0.
3. `useEffect(() => { setMyState(myState + 1); }, [myState]);` - This hook will run each time the component is rendered, and will update the `myState` variable by adding 1 to its current value.
4. `<p>My state is {myState}</p>` - This will render the value of the `myState` variable.

For more information on ReactJS Hooks, see the [React documentation](https://reactjs.org/docs/hooks-intro.html).

onelinerhub: [How can I use ReactJS Hooks to build a custom component?](https://onelinerhub.com/reactjs/how-can-i-use-reactjs-hooks-to-build-a-custom-component)