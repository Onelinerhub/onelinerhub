# How do I use the jQuery prop() method?
// plain

The jQuery `prop()` method is used to get or set the value of a property for the selected elements. It's very similar to the `attr()` method, however `prop()` should be used for properties and `attr()` should be used for attributes.

For example, to set the `checked` property of a checkbox element, you can use the following code:
```
$('#checkbox').prop('checked', true);
```

This code sets the `checked` property of the checkbox element with the id of `checkbox` to `true`.

To get the value of a property, you can use the same syntax, but without a second argument. For example, to get the `checked` property of the same checkbox element, you can use the following code:

```
var isChecked = $('#checkbox').prop('checked');
console.log(isChecked); // Outputs true
```

This code gets the `checked` property of the checkbox element with the id of `checkbox` and stores it in the `isChecked` variable.

Parts of the code and their explanation:
- `$('#checkbox')`: Selects the element with the id of `checkbox`.
- `prop('checked', true)`: Sets the `checked` property of the selected element to `true`.
- `prop('checked')`: Gets the value of the `checked` property of the selected element.
- `console.log(isChecked)`: Outputs the value of the `isChecked` variable to the console.

## Helpful links
- [jQuery prop() Documentation](https://api.jquery.com/prop/)
- [jQuery attr() Documentation](https://api.jquery.com/attr/)

onelinerhub: [How do I use the jQuery prop() method?](https://onelinerhub.com/jquery/how-do-i-use-the-jquery-prop---method)