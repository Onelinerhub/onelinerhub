# How can I use keyboard events in ReactJS?
// plain

ReactJS provides a way to handle keyboard events through the `onKeyDown` event handler. This event handler is triggered when a key is pressed down on the keyboard. It is passed an event object as an argument, which contains information about the key that was pressed.

The following is an example of using the `onKeyDown` event handler in ReactJS:

```javascript
handleKeyDown(event) {
  if (event.key === 'Enter') {
    console.log('Enter key was pressed!');
  }
}

render() {
  return (
    <div onKeyDown={this.handleKeyDown}>
      ...
    </div>
  )
}
```

The output of this code will be `Enter key was pressed!` when the enter key is pressed.

## Code explanation

1. `handleKeyDown(event)`: This is the function that handles the keydown event. It takes an `event` object as an argument, which contains information about the key that was pressed.
2. `if (event.key === 'Enter')`: This checks if the key that was pressed was the enter key.
3. `console.log('Enter key was pressed!')`: This is the action that is taken when the enter key is pressed.
4. `<div onKeyDown={this.handleKeyDown}>`: This is the element that will listen for keydown events.

## Helpful links
* [ReactJS: SyntheticEvent](https://reactjs.org/docs/events.html#syntheticevent)
* [ReactJS: Keyboard Events](https://reactjs.org/docs/events.html#keyboard-events)

onelinerhub: [How can I use keyboard events in ReactJS?](https://onelinerhub.com/reactjs/how-can-i-use-keyboard-events-in-reactjs)