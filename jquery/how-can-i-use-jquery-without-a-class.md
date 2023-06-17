# How can I use jQuery without a class?
// plain

You can use jQuery without a class by using the jQuery selector to target elements in the DOM. The jQuery selector works like a CSS selector, allowing you to target elements by their tag name, class name, or id.

For example, you can use the jQuery selector to target all `<p>` tags on a page like this:

```
$('p').css('color', 'red');
```

This code will change the color of all `<p>` tags on the page to red.

You can also use the jQuery selector to target elements by class or id. For example, if you have a class called `.my-class` and an id called `#my-id`, you could target those elements like this:

```
$('.my-class').css('background-color', 'green');
$('#my-id').css('background-color', 'blue');
```

This code will change the background color of all elements with the class `.my-class` to green and all elements with the id `#my-id` to blue.

You can also use the jQuery selector to target elements based on their attributes. For example, if you have an element with a `data-attribute` of `data-id`, you could target it like this:

```
$('[data-id]').css('font-size', '20px');
```

This code will change the font size of all elements with the `data-id` attribute to 20px.

## Helpful links
- [jQuery Selectors](https://api.jquery.com/category/selectors/)
- [jQuery Attribute Selectors](https://api.jquery.com/attribute-equals-selector/)

onelinerhub: [How can I use jQuery without a class?](https://onelinerhub.com/jquery/how-can-i-use-jquery-without-a-class)