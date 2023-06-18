# How can I use the React useContext hook?
// plain

The `useContext` hook in React allows you to access data from a context object within a functional component. This is a great way to share data between components without having to pass props through every level of the component tree.

Here is an example of using the `useContext` hook:

```js
// Context
const MyContext = React.createContext();

// Provider
const MyProvider = (props) => {
  const [state, setState] = useState({
    name: 'John Doe',
    age: 30
  });
  return (
    <MyContext.Provider value={{ state, setState }}>
      {props.children}
    </MyContext.Provider>
  )
}

// Component
const MyComponent = () => {
  const context = useContext(MyContext);
  return (
    <div>
      <p>Name: {context.state.name}</p>
      <p>Age: {context.state.age}</p>
    </div>
  )
}
```

This example creates a `MyContext` object, a `MyProvider` component, and a `MyComponent` component. The `MyProvider` component provides the `MyContext` object with a state object containing a `name` and `age` property. The `MyComponent` component then accesses this state object using the `useContext` hook.

The parts of this example are:

1. `MyContext`: the context object created using the `React.createContext()` method
2. `MyProvider`: a component that provides the `MyContext` object with a state object
3. `MyComponent`: a component that accesses the state object using the `useContext` hook

For more information on the `useContext` hook, please see the [React documentation](https://reactjs.org/docs/hooks-reference.html#usecontext).

onelinerhub: [How can I use the React useContext hook?](https://onelinerhub.com/reactjs/how-can-i-use-the-react-usecontext-hook)