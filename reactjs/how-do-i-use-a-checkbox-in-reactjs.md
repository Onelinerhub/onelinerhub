# How do I use a checkbox in ReactJS?
// plain

Using a checkbox in ReactJS is relatively simple. To start, you will need to import the `Checkbox` component from the `@material-ui/core` package.

```
import Checkbox from '@material-ui/core/Checkbox';
```

Next, you will need to define the `onChange` function for the checkbox. This function will be called when the user clicks on the checkbox.

```
const handleChange = (event) => {
  setChecked(event.target.checked);
};
```

You will also need to define the `checked` state variable and the `setChecked` function. The `checked` state variable will store the current state of the checkbox (true or false). The `setChecked` function will be used to update the state.

```
const [checked, setChecked] = React.useState(false);
```

Finally, you can render the `Checkbox` component.

```
<Checkbox
  checked={checked}
  onChange={handleChange}
  inputProps={{ 'aria-label': 'primary checkbox' }}
/>
```

This will render a checkbox with the `checked` state set to the value of the `checked` state variable, and the `onChange` function set to the `handleChange` function.

## Helpful links

- [Checkbox - Material UI](https://material-ui.com/components/checkboxes/)
- [React - Using the State Hook](https://reactjs.org/docs/hooks-state.html)

onelinerhub: [How do I use a checkbox in ReactJS?](https://onelinerhub.com/reactjs/how-do-i-use-a-checkbox-in-reactjs)