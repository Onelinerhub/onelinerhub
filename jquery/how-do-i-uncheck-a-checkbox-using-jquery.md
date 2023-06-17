# How do I uncheck a checkbox using jQuery?
// plain

To uncheck a checkbox using jQuery, you can use the `prop()` method. This method will set the property of the checkbox to `false`:

```javascript
$('input[type="checkbox"]').prop('checked', false);
```

The code above will uncheck all checkboxes on the page. To uncheck a specific checkbox, you can use the `attr()` method, passing in the `checked` attribute and setting it to `false`:

```javascript
$('#myCheckbox').attr('checked', false);
```

The code above will uncheck the checkbox with the `id` of `myCheckbox`.

## Code explanation


- `$('input[type="checkbox"]')` - This is a jQuery selector that selects all checkboxes on the page.
- `prop('checked', false)` - This is the `prop()` method that sets the `checked` property of the checkbox to `false`, thus unchecking it.
- `$('#myCheckbox')` - This is a jQuery selector that selects the checkbox with the `id` of `myCheckbox`.
- `attr('checked', false)` - This is the `attr()` method that sets the `checked` attribute of the checkbox to `false`, thus unchecking it.

Here are some ## Helpful links

- [jQuery `prop()` Method](https://api.jquery.com/prop/)
- [jQuery `attr()` Method](https://api.jquery.com/attr/)

onelinerhub: [How do I uncheck a checkbox using jQuery?](https://onelinerhub.com/jquery/how-do-i-uncheck-a-checkbox-using-jquery)