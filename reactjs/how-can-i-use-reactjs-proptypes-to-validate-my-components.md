# How can I use ReactJS PropTypes to validate my components?
// plain

ReactJS PropTypes is a built-in type-checking system used to validate the properties passed to a React component. It helps to ensure that the data passed to a component is of the expected type.

For example, the following code block defines a component with a `name` prop that is expected to be a string.

```js
import PropTypes from 'prop-types';

class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}

Welcome.propTypes = {
  name: PropTypes.string
};
```

If a component is rendered with a `name` prop that is not a string, a warning will be displayed in the console:

```
Warning: Failed prop type: Invalid prop `name` of type `number` supplied to `Welcome`, expected `string`.
```

## Code explanation


1. `import PropTypes from 'prop-types';`: imports the PropTypes library
2. `name: PropTypes.string`: specifies that the `name` prop is expected to be a string
3. `Failed prop type: Invalid prop`: the warning message displayed in the console

For more information, please refer to the [React documentation](https://reactjs.org/docs/typechecking-with-proptypes.html).

onelinerhub: [How can I use ReactJS PropTypes to validate my components?](https://onelinerhub.com/reactjs/how-can-i-use-reactjs-proptypes-to-validate-my-components)