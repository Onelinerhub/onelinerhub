# How do I create a dropdown menu in ReactJS?
// plain

To create a dropdown menu in ReactJS, you can use the `React-Select` library. It is a flexible and powerful Select control built for React.

## Example code

```
import React from 'react';
import Select from 'react-select';

const options = [
  { value: 'chocolate', label: 'Chocolate' },
  { value: 'strawberry', label: 'Strawberry' },
  { value: 'vanilla', label: 'Vanilla' }
]

class App extends React.Component {
  state = {
    selectedOption: null,
  }
  handleChange = (selectedOption) => {
    this.setState({ selectedOption });
    console.log(`Option selected:`, selectedOption);
  }
  render() {
    const { selectedOption } = this.state;

    return (
      <Select
        value={selectedOption}
        onChange={this.handleChange}
        options={options}
      />
    );
  }
}
```

This code will render a dropdown menu with the options `Chocolate`, `Strawberry`, and `Vanilla`.

The code is composed of the following parts:

1. `import React from 'react';`: This imports the React library.
2. `import Select from 'react-select';`: This imports the React-Select library.
3. `const options = [...]`: This creates an array of objects containing the options for the dropdown menu.
4. `handleChange = (selectedOption) => {...}`: This is a function that is called when the user selects an option from the dropdown menu. It sets the `selectedOption` state variable to the option that was selected.
5. `render() {...}`: This is the function that renders the React component. It uses the `Select` component from the React-Select library to render the dropdown menu.

For more information, see the [React-Select documentation](https://react-select.com/home).

onelinerhub: [How do I create a dropdown menu in ReactJS?](https://onelinerhub.com/reactjs/how-do-i-create-a-dropdown-menu-in-reactjs)