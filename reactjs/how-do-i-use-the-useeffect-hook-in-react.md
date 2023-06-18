# How do I use the useEffect hook in React?
// plain

The useEffect hook in React allows you to perform side effects in function components. It is a built-in hook that is used to perform data fetching, setting up a subscription, and manually changing the DOM in React components.

## Example

```
import React, { useEffect } from 'react';

function Example() {
  useEffect(() => {
    document.title = 'Example Title';
  });

  return (
    <div>
      <h1>Example</h1>
    </div>
  );
}
```

The example above will set the document title to `Example Title`.

The useEffect hook is composed of the following parts:

- The `useEffect` function, which is used to perform the side effect.
- The function that is passed as an argument to the `useEffect` function. This function will be called after the component is rendered.

The useEffect hook is invoked after every render, including the first render of the component. It is important to note that the function passed to `useEffect` is not called during the initial render, but only after.

## Helpful links
- [React Documentation - useEffect](https://reactjs.org/docs/hooks-reference.html#useeffect)
- [React Tutorial - useEffect](https://reactjs.org/tutorial/tutorial.html#using-hooks)

onelinerhub: [How do I use the useEffect hook in React?](https://onelinerhub.com/reactjs/how-do-i-use-the-useeffect-hook-in-react)