# How do I use jQuery to prepend HTML elements?
// plain

To use jQuery to prepend HTML elements, you must first select the element you wish to prepend to. You can do this using the `$()` function, which takes a selector as an argument. For example, `$('#example-element')` will select the element with the ID of `example-element`.

Once you have selected the element, you can use the `prepend()` function to add the HTML element you wish to prepend. This function takes a string of HTML as an argument. For example, `$('#example-element').prepend('<p>Hello world!</p>')` will prepend a `<p>` element with the text "Hello world!" to the element with the ID of `example-element`.

Below is an example of using jQuery to prepend HTML elements:

```javascript
$('#example-element').prepend('<p>Hello world!</p>');
```

The output of this code will be the element with the ID of `example-element` now containing the `<p>` element with the text "Hello world!" prepended to it.

## Code explanation

- `$('#example-element')` - This selects the element with the ID of `example-element` using the `$()` function.
- `.prepend('<p>Hello world!</p>')` - This uses the `prepend()` function to prepend the `<p>` element with the text "Hello world!" to the previously selected element.

## Helpful links
- [jQuery Prepend() Function](https://api.jquery.com/prepend/)
- [jQuery Selectors](https://api.jquery.com/category/selectors/)

onelinerhub: [How do I use jQuery to prepend HTML elements?](https://onelinerhub.com/jquery/how-do-i-use-jquery-to-prepend-html-elements)