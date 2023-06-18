# down event

How can I handle a keydown event in ReactJS?
// plain

The keydown event in ReactJS can be handled using the `onKeyDown` event handler. This event handler is triggered when a key is pressed down while the React component is in focus.

For example:

```
class MyComponent extends React.Component {
  handleKeyDown = (event) => {
    console.log('Key pressed: ', event.key);
  }

  render() {
    return (
      <div tabIndex="0" onKeyDown={this.handleKeyDown}>
        Press a key!
      </div>
    );
  }
}
```

When a key is pressed while the component is in focus, the `handleKeyDown` function will be called and the `event.key` property will be logged to the console.

The following parts are included in the example code:

1. `handleKeyDown` - a function that is triggered when the `onKeyDown` event handler is called. It logs the `event.key` property to the console.
2. `onKeyDown` - an event handler that is triggered when a key is pressed while the component is in focus.
3. `tabIndex` - a property that allows the component to be focused by the user.

## Helpful links

- [React SyntheticEvent](https://reactjs.org/docs/events.html#syntheticevent)
- [onKeyDown](https://reactjs.org/docs/events.html#onkeydown)
- [tabIndex](https://reactjs.org/docs/dom-elements.html#tabindex)

onelinerhub: [down event

How can I handle a keydown event in ReactJS?](https://onelinerhub.com/reactjs/down-event--how-can-i-handle-a-keydown-event-in-reactjs)