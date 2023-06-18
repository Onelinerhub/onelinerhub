# How do I use a timer in ReactJS?
// plain

Using a timer in ReactJS is relatively simple. To do so, you can create a new React component and use the built-in JavaScript `setTimeout()` method. The `setTimeout()` method takes two arguments - a callback function and the amount of time in milliseconds before the callback function is executed.

```javascript
// Example of using setTimeout() in React
class Timer extends React.Component {
  constructor(props) {
    super(props);
    this.state = { seconds: 0 };
  }
  componentDidMount() {
    this.timerID = setTimeout(
      () => this.tick(),
      1000
    );
  }
  componentWillUnmount() {
    clearTimeout(this.timerID);
  }
  tick() {
    this.setState({
      seconds: this.state.seconds + 1
    });
    this.timerID = setTimeout(
      () => this.tick(),
      1000
    );
  }
  render() {
    return (
      <div>
        Seconds: {this.state.seconds}
      </div>
    );
  }
}

ReactDOM.render(
  <Timer />,
  document.getElementById('root')
);
```

## Output example

```
Seconds: 0
```

The code above creates a Timer component which uses the `setTimeout()` method to increment the `seconds` state value by 1 every second. The `setTimeout()` method is called inside the `componentDidMount()` lifecycle method which is called when the component is mounted and the `componentWillUnmount()` lifecycle method which is called when the component is unmounted.

## Code explanation

- `constructor()`: The constructor method is used to set the initial state of the component.
- `componentDidMount()`: This is a lifecycle method that is called when the component is mounted.
- `componentWillUnmount()`: This is a lifecycle method that is called when the component is unmounted.
- `tick()`: This is a method which is called every second to increment the `seconds` state value.
- `setTimeout()`: This is a built-in JavaScript method which takes a callback function and the amount of time in milliseconds before the callback function is executed.
- `clearTimeout()`: This is a built-in JavaScript method which clears the timer set with `setTimeout()`.

## Helpful links
- [React Documentation - Timers](https://reactjs.org/docs/timers.html)
- [MDN - setTimeout()](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)
- [MDN - clearTimeout()](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/clearTimeout)

onelinerhub: [How do I use a timer in ReactJS?](https://onelinerhub.com/reactjs/how-do-i-use-a-timer-in-reactjs)