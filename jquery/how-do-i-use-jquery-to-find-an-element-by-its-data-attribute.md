# How do I use jQuery to find an element by its data attribute?
// plain

To find an element by its data attribute using jQuery, you can use the `.data()` method. This method takes the data attribute name as the argument and returns the value of the attribute. For example, to find an element with a data attribute of `data-name`:

```
var name = $('#myElement').data('name');
```

This will return the value of the `data-name` attribute from the element with the id of `myElement`.

## Code explanation


- `.data()` - the jQuery method used to find an element by its data attribute
- `data-name` - the data attribute name used in the example
- `$('#myElement')` - the jQuery selector used to select the element with the id of `myElement`
- `name` - the variable used to store the value of the `data-name` attribute

## Helpful links

- [jQuery .data() Method](https://api.jquery.com/data/)

onelinerhub: [How do I use jQuery to find an element by its data attribute?](https://onelinerhub.com/jquery/how-do-i-use-jquery-to-find-an-element-by-its-data-attribute)