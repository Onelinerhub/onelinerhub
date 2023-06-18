# How can I use the useRef hook with React and TypeScript?
// plain

The useRef hook is a React hook that provides a way to access the underlying DOM element or React component that is rendered to the DOM. It can be used with React and TypeScript to access the DOM element or React component in a type-safe manner.

The following example demonstrates how to use useRef hook with React and TypeScript:

```
import React, { useRef } from 'react';

interface Props {
  text: string;
}

const Example: React.FC<Props> = ({ text }) => {
  const ref = useRef<HTMLDivElement>(null);

  return (
    <div ref={ref}>
      {text}
    </div>
  );
};
```

In the example above:

1. We import React and useRef from the React library.
2. We define an interface for the component props.
3. We create a functional component and pass in the props.
4. We declare a ref variable and assign it the result of useRef.
5. We pass the ref variable to the div element as a ref attribute.

This allows us to access the underlying DOM element or React component in a type-safe manner.

## Helpful links

- [React Docs - useRef](https://reactjs.org/docs/hooks-reference.html#useref)
- [TypeScript Docs - useRef](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-8.html#support-for-react-hooks)

onelinerhub: [How can I use the useRef hook with React and TypeScript?](https://onelinerhub.com/reactjs/how-can-i-use-the-useref-hook-with-react-and-typescript)