# How do I select the last child element using jQuery?
// plain

The last child element can be selected using jQuery by using the `:last-child` selector. This selector will select the last element within its parent element. For example, if you have a list of items, the `:last-child` selector will select the last item in the list.

## Example code

```
$('ul li:last-child').css('color', 'red');
```

This code will select the last `li` within the `ul` element, and apply a `color` of `red` to it.

## Code explanation

- `$('ul li:last-child')`: This will select the last `li` element within the `ul` element.
- `.css('color', 'red')`: This will apply a `color` of `red` to the selected element.

## Helpful links
- [jQuery Selectors](https://api.jquery.com/category/selectors/)
- [jQuery .css()](https://api.jquery.com/css/)

onelinerhub: [How do I select the last child element using jQuery?](https://onelinerhub.com/jquery/how-do-i-select-the-last-child-element-using-jquery)