# How do I create a "Hello World" application with ReactJS?
// plain

Creating a "Hello World" application with ReactJS is a great way to get familiar with the basics of React. To do this, you'll need to create a React component that will render the text "Hello World". Here is an example of how to do this:

```
import React from 'react';

class HelloWorld extends React.Component {
  render() {
    return (
      <h1>Hello World</h1>
    );
  }
}

export default HelloWorld;
```

This code creates a React component called `HelloWorld` that renders the text "Hello World". It does this by importing the `React` library and creating a `HelloWorld` class that extends the `React.Component` class. The `render()` method of this class is then used to return the HTML element `<h1>Hello World</h1>`.

## Code explanation


- `import React from 'react';`: imports the React library
- `class HelloWorld extends React.Component {...}`: creates a React component called `HelloWorld`
- `render() {...}`: the `render()` method of the `HelloWorld` class is used to return the HTML element `<h1>Hello World</h1>`
- `export default HelloWorld;`: exports the `HelloWorld` component so that it can be used in other files

For more information about React components, please see the [React documentation](https://reactjs.org/docs/components-and-props.html).

onelinerhub: [How do I create a "Hello World" application with ReactJS?](https://onelinerhub.com/reactjs/how-do-i-create-a--hello-world--application-with-reactjs)