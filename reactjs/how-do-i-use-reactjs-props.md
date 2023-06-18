# How do I use ReactJS props?
// plain

Props are a way of passing data from a parent component to a child component in React. Props are read-only and should not be modified within the child component.

## Example


```
// Parent Component
import React from 'react';
import ChildComponent from './ChildComponent';

class ParentComponent extends React.Component {
  render() {
    return (
      <ChildComponent message="Hello World!" />
    )
  }
}

export default ParentComponent;

// Child Component
import React from 'react';

class ChildComponent extends React.Component {
  render() {
    return (
      <div>
        {this.props.message}
      </div>
    )
  }
}

export default ChildComponent;
```
## Output example


Hello World!

The code above is composed of two components, the ParentComponent and the ChildComponent. In the ParentComponent, a prop called `message` is passed to the ChildComponent. In the ChildComponent, the `message` prop is accessed via `this.props.message` and rendered to the screen.

## Code explanation


1. `import React from 'react'`: This line imports the React library, which is necessary for writing React components.
2. `class ParentComponent extends React.Component`: This line creates a new React component called ParentComponent, which is a subclass of React.Component.
3. `<ChildComponent message="Hello World!" />`: This line renders the ChildComponent, passing in a prop called `message` with a value of `Hello World!`.
4. `class ChildComponent extends React.Component`: This line creates a new React component called ChildComponent, which is a subclass of React.Component.
5. `this.props.message`: This line accesses the `message` prop that was passed into the ChildComponent.
6. `<div>{this.props.message}</div>`: This line renders the value of the `message` prop inside of a div.

## Helpful links
- [React Props Overview](https://reactjs.org/docs/components-and-props.html)
- [React Props Tutorial](https://www.tutorialspoint.com/reactjs/reactjs_props.htm)

onelinerhub: [How do I use ReactJS props?](https://onelinerhub.com/reactjs/how-do-i-use-reactjs-props)