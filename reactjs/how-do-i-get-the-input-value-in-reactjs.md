# How do I get the input value in ReactJS?
// plain

In ReactJS, you can get the input value by using the `onChange` event handler and using the `event.target.value` property.

## Example code

```
import React from 'react';

class MyInput extends React.Component {
  constructor() {
    super();
    this.state = {
      inputValue: ''
    };
  }

  handleChange = (event) => {
    this.setState({
      inputValue: event.target.value
    });
  }

  render() {
    return (
      <input
        type="text"
        value={this.state.inputValue}
        onChange={this.handleChange}
      />
    );
  }
}
```

In the example code above, the `onChange` event handler is used to update the `inputValue` state with the `event.target.value` property. This will update the `inputValue` state every time the value of the input field is changed.

## Code explanation

- `import React from 'react'`: This imports the React library.
- `constructor()`: This is the constructor of the component and is used to set the initial state of the `inputValue` to an empty string.
- `handleChange = (event) => {...}`: This is the event handler for the `onChange` event. It is used to update the `inputValue` state with the `event.target.value` property.
- `<input type="text" value={this.state.inputValue} onChange={this.handleChange} />`: This is the input field which will be rendered. The `value` prop is set to the `inputValue` state and the `onChange` prop is set to the `handleChange` event handler.

## Helpful links
- [React - Getting Started](https://reactjs.org/docs/getting-started.html)
- [React - SyntheticEvent](https://reactjs.org/docs/events.html#syntheticevent)

onelinerhub: [How do I get the input value in ReactJS?](https://onelinerhub.com/reactjs/how-do-i-get-the-input-value-in-reactjs)