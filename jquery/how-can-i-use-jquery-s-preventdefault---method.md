# How can I use jQuery's preventDefault() method?
// plain

The `preventDefault()` method in jQuery can be used to prevent the default action of an element from happening. This can be useful when you want to control the behavior of an element, such as a form submission or a link click.

For example, the following code will prevent the default action of a link from happening when it is clicked:

```javascript
$('a').click(function(e){
    e.preventDefault();
});
```

This code will prevent the link from taking the user to the URL specified in the `href` attribute of the link.

The `preventDefault()` method can also be used to prevent the default action of a form submission. For example, the following code will prevent the form from being submitted when the submit button is clicked:

```javascript
$('form').submit(function(e){
    e.preventDefault();
});
```

This code will prevent the form data from being sent to the server and the page from reloading.

The `preventDefault()` method takes an event object as an argument, which can be obtained by passing an event handler function to the element's event handler.

## Code explanation


- `$('a').click(function(e)`: This assigns a click event handler to all `<a>` elements.
- `e.preventDefault()`: This calls the `preventDefault()` method on the event object to prevent the default action from happening.

Here is a list of ## Helpful links

- [jQuery's preventDefault() Method](https://api.jquery.com/event.preventdefault/)
- [jQuery Event Handlers](https://www.w3schools.com/jquery/jquery_events.asp)

onelinerhub: [How can I use jQuery's preventDefault() method?](https://onelinerhub.com/jquery/how-can-i-use-jquery-s-preventdefault---method)