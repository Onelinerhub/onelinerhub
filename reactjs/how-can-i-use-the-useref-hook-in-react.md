# How can I use the useRef hook in React?
// plain

The useRef hook in React allows you to create a reference to a DOM element or a React component instance. This can be useful when you need to access the DOM element or the React component instance programmatically, for example to focus on an input element or to set a value of a React component instance.

## Example


```
const inputRef = useRef(null);

// set the inputRef to the DOM element
inputRef.current = document.querySelector("input");

// set the focus on the input element
inputRef.current.focus();
```

The useRef hook is also useful for storing mutable values that you want to persist between renders.

## Example


```
const count = useRef(0);

// increment the count
count.current += 1;

// log the current count
console.log(count.current); // 1
```

The useRef hook is particularly useful for storing values that you want to persist between renders, such as the current value of a form input or the current state of a React component instance.

## Helpful links
- [React Docs - useRef](https://reactjs.org/docs/hooks-reference.html#useref)
- [CSS Tricks - useRef in React](https://css-tricks.com/using-refs-in-react/)

onelinerhub: [How can I use the useRef hook in React?](https://onelinerhub.com/reactjs/how-can-i-use-the-useref-hook-in-react)