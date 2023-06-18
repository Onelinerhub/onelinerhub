# How do I implement a year picker using ReactJS?
// plain

To implement a year picker using ReactJS, you can use the [react-datepicker](https://reactdatepicker.com/) library.

It provides a `<DatePicker />` component which can be used to select a year. The following example code shows how to use it:

```js
import DatePicker from "react-datepicker";

<DatePicker
  selected={this.state.startDate}
  onChange={this.handleChange}
  showYearDropdown
  dateFormat="yyyy"
/>
```

This will render a year picker which allows the user to select a year. The `showYearDropdown` prop is used to show the year dropdown and the `dateFormat` prop is used to set the format of the date.

## Code explanation

- `import DatePicker from "react-datepicker"`: This imports the DatePicker component from the react-datepicker library.
- `<DatePicker selected={this.state.startDate}`: This renders the DatePicker component and sets the currently selected date to `this.state.startDate`.
- `onChange={this.handleChange}`: This sets the `onChange` callback which is called when the user selects a date.
- `showYearDropdown`: This prop is used to show the year dropdown.
- `dateFormat="yyyy"`: This sets the format of the date to `yyyy` which will show only the year.

For more information, you can refer to the [react-datepicker documentation](https://reactdatepicker.com/).

onelinerhub: [How do I implement a year picker using ReactJS?](https://onelinerhub.com/reactjs/how-do-i-implement-a-year-picker-using-reactjs)