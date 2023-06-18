# How do I use ReactJS events to handle user interactions?
// plain

ReactJS events are used to handle user interactions such as mouse clicks, key presses, and form submissions. React provides a SyntheticEvent wrapper for cross-browser compatibility. To use ReactJS events, you must add an event listener to a component using the `on[event]` syntax. For example, to handle a mouse click event, you would use the `onClick` event listener.

```
class MyComponent extends React.Component {
  handleClick() {
    alert('Button clicked!');
  }

  render() {
    return (
      <button onClick={this.handleClick}>
        Click Me
      </button>
    );
  }
}
```

When the button is clicked, the `handleClick()` function is called and the alert is displayed.

## Code explanation


1. `class MyComponent extends React.Component`: This declares the component class.
2. `handleClick() { alert('Button clicked!'); }`: This is the event handler function that is called when the button is clicked.
3. `onClick={this.handleClick}`: This is the event listener that is added to the button and calls the event handler function when the button is clicked.

For more information, see the [ReactJS Events documentation](https://reactjs.org/docs/events.html).

onelinerhub: [How do I use ReactJS events to handle user interactions?](https://onelinerhub.com/reactjs/how-do-i-use-reactjs-events-to-handle-user-interactions)