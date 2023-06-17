# How can I convert jQuery code to vanilla JavaScript?
// plain

The conversion of jQuery code to vanilla JavaScript requires understanding of the underlying JavaScript code that jQuery is written in. In most cases, the jQuery code can be replaced by the equivalent JavaScript functions.

For example, the following jQuery code:
```
$('#myDiv').hide();
```
Can be converted to the following vanilla JavaScript code:
```
document.getElementById('myDiv').style.display = 'none';
```

## Code explanation

- `$('#myDiv')`: This is a jQuery function that selects an element with the specified id.
- `hide()`: This is a jQuery function that hides the selected element.

In vanilla JavaScript, the equivalent functions are:
- `document.getElementById('myDiv')`: This is a JavaScript function that selects an element with the specified id.
- `style.display = 'none'`: This is a JavaScript function that sets the display style of the selected element to 'none', which hides the element.

For more information on converting jQuery code to vanilla JavaScript, see the following resources:
- [jQuery to Vanilla JS](https://vanillajstoolkit.com/jquery-to-vanilla-js/)
- [You Might Not Need jQuery](http://youmightnotneedjquery.com/)

onelinerhub: [How can I convert jQuery code to vanilla JavaScript?](https://onelinerhub.com/jquery/how-can-i-convert-jquery-code-to-vanilla-javascript)