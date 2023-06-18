# component

How do I create an input component using ReactJS?
// plain

Creating an input component using ReactJS is a simple task. First, import the `useState` hook from the React library. This hook allows us to store state in the component.

```
import React, { useState } from 'react';
```

Next, create the component function with an argument of `props` which will contain the properties of the component. Inside the component function, create a variable to hold the state of the input field using the `useState` hook.

```
function InputComponent(props) {
  const [inputValue, setInputValue] = useState('');
}
```

Then, create the input element which will contain the value of the state variable. The `onChange` event handler is used to update the state variable when the value of the input element changes.

```
<input
  type="text"
  value={inputValue}
  onChange={(e) => setInputValue(e.target.value)}
/>
```

Finally, return the input element from the component function.

```
return <input
  type="text"
  value={inputValue}
  onChange={(e) => setInputValue(e.target.value)}
/>
```

The output of the component will be an input field that can be used to capture user input.

## Helpful links
- [React useState Hook](https://reactjs.org/docs/hooks-reference.html#usestate)
- [React Input Element](https://reactjs.org/docs/forms.html#controlled-components)

onelinerhub: [component

How do I create an input component using ReactJS?](https://onelinerhub.com/reactjs/component--how-do-i-create-an-input-component-using-reactjs)