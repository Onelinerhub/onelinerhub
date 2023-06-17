# How do I check a checkbox using jQuery?
// plain

To check a checkbox using jQuery, you can use the `.prop()` method. This method is used to set or return the properties and values of the selected elements.

Below is an example of jQuery code to check a checkbox:
```
$('#checkbox').prop('checked', true);
```
This code will check the checkbox with the `id="checkbox"`.

The code above consists of two parts:
1. `$('#checkbox')` - this is a jQuery selector that selects the element with the `id="checkbox"`
2. `.prop('checked', true)` - this is the jQuery method used to set the `checked` property of the selected element to `true`

After running the code, the checkbox will be checked.

## Helpful links
- [jQuery .prop() Method](https://www.w3schools.com/jquery/jquery_dom_set.asp)

onelinerhub: [How do I check a checkbox using jQuery?](https://onelinerhub.com/jquery/how-do-i-check-a-checkbox-using-jquery)