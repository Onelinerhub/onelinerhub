# How do I use the useMemo hook in React?
// plain

The `useMemo` hook is a React hook that allows you to store a value and return it when a condition is met. It is useful for optimizing performance by avoiding expensive calculations on every render.

Here is an example of how to use `useMemo`:

```js
const [count, setCount] = useState(0);
const expensiveCalculation = useMemo(() => {
  let result = 0;
  // some expensive calculations
  for (let i = 0; i < count; i++) {
    result += i;
  }
  return result;
}, [count]);

return (
  <div>
    <h1>{expensiveCalculation}</h1>
    <button onClick={() => setCount(count + 1)}>
      Increment
    </button>
  </div>
);
```

In the example above, the `useMemo` hook is used to store the result of the expensive calculation. The hook takes a function as its first argument and an array of dependencies as its second argument. The function will be called when the values in the dependencies array change. In this example, the function will be called when the value of `count` changes.

The output of the example code is a div with a heading showing the result of the expensive calculation and a button that increments the count.

Here are some ## Helpful links

- [React Documentation on useMemo](https://reactjs.org/docs/hooks-reference.html#usememo)
- [Blog post on useMemo](https://dmitripavlutin.com/react-usememo-hook/)

onelinerhub: [How do I use the useMemo hook in React?](https://onelinerhub.com/reactjs/how-do-i-use-the-usememo-hook-in-react)