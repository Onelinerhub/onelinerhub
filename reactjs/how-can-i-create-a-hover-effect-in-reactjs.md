# How can I create a hover effect in ReactJS?
// plain

The hover effect can be created in ReactJS by using the onMouseEnter and onMouseLeave events. The following example code block shows how to create a hover effect in ReactJS:

```
import React from "react";

class HoverEffect extends React.Component {
  state = {
    hover: false
  };

  mouseEnter = () => {
    this.setState({ hover: true });
  };

  mouseLeave = () => {
    this.setState({ hover: false });
  };

  render() {
    return (
      <div
        onMouseEnter={this.mouseEnter}
        onMouseLeave={this.mouseLeave}
      >
        {this.state.hover ? "Hovering!" : "Not Hovering!"}
      </div>
    );
  }
}
```

## Output example
 Not Hovering!

## Code explanation


1. `import React from "react";` - Imports the React library.
2. `state = {hover: false};` - Sets the initial state of the hover effect to false.
3. `mouseEnter = () => {this.setState({ hover: true });};` - Sets the state of the hover effect to true when the mouse enters the element.
4. `mouseLeave = () => {this.setState({ hover: false });};` - Sets the state of the hover effect to false when the mouse leaves the element.
5. `onMouseEnter={this.mouseEnter}` - Calls the mouseEnter function when the mouse enters the element.
6. `onMouseLeave={this.mouseLeave}` - Calls the mouseLeave function when the mouse leaves the element.
7. `this.state.hover ? "Hovering!" : "Not Hovering!"` - Displays the text "Hovering!" or "Not Hovering!" depending on the state of the hover effect.

## Helpful links
- [React Docs - Handling Events](https://reactjs.org/docs/handling-events.html)
- [React Docs - Conditional Rendering](https://reactjs.org/docs/conditional-rendering.html)

onelinerhub: [How can I create a hover effect in ReactJS?](https://onelinerhub.com/reactjs/how-can-i-create-a-hover-effect-in-reactjs)