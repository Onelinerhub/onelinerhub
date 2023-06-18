# How do I use ReactJS setState to update my component's state?
// plain

`ReactJS setState` is an important function used to update the state of a React component. The setState function takes two parameters: an object containing the new state values and a callback function that is called once the state has been updated.

To use ReactJS setState to update a component's state, you must first create a class-based component and define the initial state. For example:

```js
class Example extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0
    };
  }
  ...
}
```

Then you can call the setState function to update the state of the component. For example:

```js
this.setState({ count: this.state.count + 1 });
```

This will update the `count` state value to be one more than its current value.

You can also pass a callback function as the second parameter to the setState function. This callback will be called after the state has been updated. For example:

```js
this.setState({ count: this.state.count + 1 }, () => {
  console.log('State updated');
});

// Output: State updated
```

The callback function can be used to perform any additional tasks that need to be done after the state has been updated.

ReactJS setState is an important function for updating the state of a React component. It takes two parameters: an object containing the new state values and a callback function that is called once the state has been updated.

## Helpful links

- [React Docs: setState](https://reactjs.org/docs/react-component.html#setstate)
- [React Docs: State and Lifecycle](https://reactjs.org/docs/state-and-lifecycle.html)

onelinerhub: [How do I use ReactJS setState to update my component's state?](https://onelinerhub.com/reactjs/how-do-i-use-reactjs-setstate-to-update-my-component-s-state)