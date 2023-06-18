# How do you use React.js to create an onhover effect?
// plain

React.js can be used to create an onhover effect by using the onMouseEnter and onMouseLeave event handlers. These event handlers can be used to call a function when the mouse enters or leaves the component. The function can then update the state of the component to display the desired effect.

For example, the following code will display a message when the mouse enters the component:

```
class MyComponent extends React.Component {
  state = {
    message: ""
  };

  handleMouseEnter = () => {
    this.setState({
      message: "Mouse is over the component"
    });
  };

  handleMouseLeave = () => {
    this.setState({
      message: ""
    });
  };

  render() {
    return (
      <div
        onMouseEnter={this.handleMouseEnter}
        onMouseLeave={this.handleMouseLeave}
      >
        {this.state.message}
      </div>
    );
  }
}
```

The component will display the message `Mouse is over the component` when the mouse is over the component.

## Code explanation

- `state`: holds the message that will be displayed when the mouse is over the component
- `handleMouseEnter`: a function that updates the state to display the message when the mouse enters the component
- `handleMouseLeave`: a function that updates the state to hide the message when the mouse leaves the component
- `onMouseEnter` and `onMouseLeave`: event handlers that call the functions when the mouse enters or leaves the component

## Helpful links
- [React Documentation - Handling Events](https://reactjs.org/docs/handling-events.html)
- [React Documentation - Using the State Hook](https://reactjs.org/docs/hooks-state.html)

onelinerhub: [How do you use React.js to create an onhover effect?](https://onelinerhub.com/reactjs/how-do-you-use-react-js-to-create-an-onhover-effect)