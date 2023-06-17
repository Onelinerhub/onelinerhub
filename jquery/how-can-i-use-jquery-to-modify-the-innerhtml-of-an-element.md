# How can I use jQuery to modify the innerHTML of an element?
// plain

You can use jQuery to modify the innerHTML of an element by using the `.html()` method. The `.html()` method takes a string as an argument which will replace the content of the element.

## Example

```
$('#example').html('This is a new string');
```

This code will replace the content of the element with the id of `example` with the string `This is a new string`.

## Code explanation

- `$('#example')`: This is a jQuery selector which will select the element with the id of `example`.
- `.html()`: This is the jQuery method which will modify the innerHTML of the element.
- `'This is a new string'`: This is the argument passed to the `.html()` method which will be the new content of the element.

## Helpful links
- [jQuery .html() Method](https://www.w3schools.com/jquery/html_html.asp)

onelinerhub: [How can I use jQuery to modify the innerHTML of an element?](https://onelinerhub.com/jquery/how-can-i-use-jquery-to-modify-the-innerhtml-of-an-element)