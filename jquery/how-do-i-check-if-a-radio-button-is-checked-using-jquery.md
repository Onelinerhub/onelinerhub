# How do I check if a radio button is checked using jQuery?
// plain

To check if a radio button is checked using jQuery, you can use the `:checked` selector in combination with the `.prop()` method. The following example code will return `true` if the radio button with the ID `myRadio` is checked:

```javascript
var isChecked = $("#myRadio").prop("checked");
console.log(isChecked); // Output: true
```

The code consists of the following parts:

1. `$("#myRadio")` - This is a jQuery selector which selects the element with the ID `myRadio`.
2. `.prop("checked")` - This is a jQuery method which gets the value of the `checked` property of the selected element.
3. `var isChecked` - This is a variable which will store the value of the `checked` property.
4. `console.log(isChecked)` - This is a console method which logs the value of the `isChecked` variable.

## Helpful links

- [jQuery :checked Selector](https://api.jquery.com/checked-selector/)
- [jQuery .prop() Method](https://api.jquery.com/prop/)

onelinerhub: [How do I check if a radio button is checked using jQuery?](https://onelinerhub.com/jquery/how-do-i-check-if-a-radio-button-is-checked-using-jquery)