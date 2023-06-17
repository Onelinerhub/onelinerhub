# How do I use jQuery to get the selected option?
// plain

The `.val()` method in jQuery can be used to get the selected option from a dropdown list. To use this method, the selector for the dropdown list is passed as an argument to the `.val()` method. The following example code block demonstrates the use of the `.val()` method:

```javascript
var selectedOption = $('#dropdownList').val();
console.log(selectedOption);
```

The output of the above code is the value of the selected option from the dropdown list:

```
Option3
```

The code can be broken down into the following parts:

1. `$('#dropdownList')`: This is the selector for the dropdown list.

2. `.val()`: This is the method used to get the selected option from the dropdown list.

3. `var selectedOption`: This is the variable used to store the value of the selected option.

4. `console.log(selectedOption)`: This is used to log the value of the selected option to the console.

## Helpful links

- [jQuery .val() Method](https://api.jquery.com/val/)

onelinerhub: [How do I use jQuery to get the selected option?](https://onelinerhub.com/jquery/how-do-i-use-jquery-to-get-the-selected-option)