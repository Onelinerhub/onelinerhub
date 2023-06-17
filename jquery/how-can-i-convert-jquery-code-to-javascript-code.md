# How can I convert jQuery code to JavaScript code?
// plain

Converting jQuery code to JavaScript code can be done by understanding the difference between the two languages. jQuery is a library of JavaScript functions that are used to simplify DOM manipulation and event handling. The following example code shows how to convert a jQuery statement into JavaScript:

```
// jQuery
$('#myDiv').hide();

// JavaScript
document.getElementById('myDiv').style.display = 'none';
```

The jQuery code uses the `$` symbol to select an element by its id, while the JavaScript code uses the `document.getElementById` method to select the same element. The jQuery code then uses the `hide()` method to hide the element, while the JavaScript code uses the `style.display` property to set the element's display to `none`.

## Code explanation


- `$('#myDiv')`: Selects the element with the id `myDiv`
- `hide()`: Hides the selected element
- `document.getElementById('myDiv')`: Selects the element with the id `myDiv`
- `style.display`: Sets the display property of the selected element

For more information on converting jQuery code to JavaScript, see the following links:

- [How to convert jQuery to JavaScript](https://www.sitepoint.com/jquery-to-javascript/)
- [Converting jQuery to JavaScript](https://www.digitalocean.com/community/tutorials/converting-jquery-to-vanilla-javascript)

onelinerhub: [How can I convert jQuery code to JavaScript code?](https://onelinerhub.com/jquery/how-can-i-convert-jquery-code-to-javascript-code)