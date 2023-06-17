# How do I use jQuery to get the value of an input field?
// plain

The jQuery `.val()` method is used to get the value of an input field. Here is an example:

```
// Get the value of an input field
var inputValue = $('#inputField').val();

// Output
console.log(inputValue); // Outputs whatever the user has typed in
```

The `#inputField` is the id of the input field. The `$('#inputField').val();` line is used to get the value of the input field and store it in the `inputValue` variable. The `console.log(inputValue);` line is used to output the value of `inputValue` to the console.

The parts of the code are:
- `$('#inputField').val();`: gets the value of the input field
- `var inputValue = `: declares a variable to store the value of the input field
- `console.log(inputValue);`: outputs the value of the variable to the console

## Helpful links
- [jQuery .val() Method](https://api.jquery.com/val/)
- [jQuery Selectors](https://api.jquery.com/category/selectors/)

onelinerhub: [How do I use jQuery to get the value of an input field?](https://onelinerhub.com/jquery/how-do-i-use-jquery-to-get-the-value-of-an-input-field)