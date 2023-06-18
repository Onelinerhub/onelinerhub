# How do I create a form using ReactJS?
// plain

Creating a form using ReactJS is fairly straightforward. To start, you need to create a `<form>` element to contain the form elements. Inside the `<form>` element, you can add any HTML input elements you need, such as `<input>`, `<select>`, or `<textarea>`.

For example:
```
<form>
  <label>Name:</label>
  <input type="text" name="name" />
  <label>Age:</label>
  <input type="number" name="age" />
  <input type="submit" value="Submit" />
</form>
```

To add React functionality to the form, you need to add a state object and a `handleChange()` method to the component. The state object should contain the values of the form, while the `handleChange()` method should update the state object when the form values change.

For example:
```
state = {
  name: '',
  age: ''
}

handleChange = (event) => {
  this.setState({
    [event.target.name]: event.target.value
  });
}
```

Finally, you need to add the `value` and `onChange` attributes to the form elements. The `value` attribute should be set to the corresponding value in the state object, while the `onChange` attribute should be set to the `handleChange()` method.

For example:
```
<input type="text" name="name" value={this.state.name} onChange={this.handleChange} />
<input type="number" name="age" value={this.state.age} onChange={this.handleChange} />
```

## Helpful links
- [Official React Docs - Forms](https://reactjs.org/docs/forms.html)
- [React Tutorial - Forms](https://reactjs.org/tutorial/tutorial.html#wrapping-up)

onelinerhub: [How do I create a form using ReactJS?](https://onelinerhub.com/reactjs/how-do-i-create-a-form-using-reactjs)