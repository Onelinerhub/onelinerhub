# How do I copy an element using jQuery?
// plain

The jQuery `.clone()` method allows you to copy an element and its contents. The syntax for the method is as follows:
```
$(selector).clone(true);
```
The `true` argument indicates that the event handlers and data associated with the element should be copied as well.

For example, to clone a `<div>` element with the id `example`:
```
var clonedDiv = $('#example').clone(true);
```
This will create a copy of the `<div>` element with all of its associated event handlers and data.

The parts of the code are as follows:
- `$('#example')`: This is a jQuery selector that selects the element with the id `example`.
- `.clone(true)`: This is the jQuery clone method that will copy the element and its contents.
- `var clonedDiv`: This is the variable that will store the cloned element.

## Helpful links
- [jQuery .clone() Documentation](https://api.jquery.com/clone/)

onelinerhub: [How do I copy an element using jQuery?](https://onelinerhub.com/jquery/how-do-i-copy-an-element-using-jquery)