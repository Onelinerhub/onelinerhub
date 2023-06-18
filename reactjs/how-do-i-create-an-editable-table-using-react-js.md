# How do I create an editable table using React.js?
// plain

Creating an editable table using React.js requires the use of components, state, and props. Here is an example of how to create an editable table with React.js:

```
class EditableTable extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [
        {name: 'John', age: '20'},
        {name: 'Jane', age: '25'},
      ]
    };
  }

  handleEdit = (rowIndex, columnIndex, newValue) => {
    let data = this.state.data;
    data[rowIndex][columnIndex] = newValue;
    this.setState({ data });
  }

  render() {
    return (
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Age</th>
          </tr>
        </thead>
        <tbody>
          {this.state.data.map((row, rowIndex) => (
            <tr key={rowIndex}>
              {Object.keys(row).map((column, columnIndex) => (
                <EditableCell
                  key={columnIndex}
                  value={row[column]}
                  onEdit={(newValue) => this.handleEdit(rowIndex, columnIndex, newValue)}
                />
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    );
  }
}
```

This example code creates a table with two columns, "Name" and "Age", and two rows of data. The `EditableTable` component contains the `data` state, which is an array of objects with the properties "name" and "age". The `render()` method renders a table with `EditableCell` components as its cells. The `EditableCell` component receives `value` and `onEdit` props, which are used to render the cell's value and handle the editing of the cell. The `handleEdit` method is used to update the `data` state when a cell is edited, and the new value is passed to the `EditableCell` component as the `onEdit` prop.

The parts of the code are as follows:

- `EditableTable` component: contains `data` state and `handleEdit` and `render` methods
- `handleEdit` method: updates `data` state when a cell is edited
- `render` method: renders a table with `EditableCell` components
- `EditableCell` component: receives `value` and `onEdit` props for rendering and handling cell editing

## Helpful links

- [React Components](https://reactjs.org/docs/components-and-props.html)
- [React State](https://reactjs.org/docs/state-and-lifecycle.html)
- [React Props](https://reactjs.org/docs/components-and-props.html)

onelinerhub: [How do I create an editable table using React.js?](https://onelinerhub.com/reactjs/how-do-i-create-an-editable-table-using-react-js)