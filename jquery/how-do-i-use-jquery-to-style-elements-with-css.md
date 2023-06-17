# How do I use jQuery to style elements with CSS?
// plain

jQuery is a JavaScript library that simplifies HTML DOM tree traversal and manipulation, as well as event handling, CSS animation, and Ajax. jQuery can be used to style elements with CSS by using the `.css()` method. This method takes an object containing the CSS properties and values to be applied to the selected elements.

For example, the following code will apply a `background-color` of `red` to all `div` elements with the class `example`:
```javascript
$('.example').css({
  'background-color': 'red'
});
```

The `.css()` method can also take a single string argument, which is the name of the CSS property to be applied. In that case, the value of the CSS property is returned. For example, the following code will return the `background-color` of the first `div` element with the class `example`:
```javascript
$('.example').first().css('background-color'); // 'red'
```

The `.css()` method can also be used to animate elements. It takes an object containing the CSS properties and values to be animated, as well as an optional duration and easing function. For example, the following code will animate the `opacity` of all `div` elements with the class `example` to 0 over the course of 1 second:
```javascript
$('.example').css({
  'opacity': 0
}, 1000);
```

## Helpful links

- [jQuery Documentation - .css()](https://api.jquery.com/css/)
- [jQuery Documentation - .animate()](https://api.jquery.com/animate/)

onelinerhub: [How do I use jQuery to style elements with CSS?](https://onelinerhub.com/jquery/how-do-i-use-jquery-to-style-elements-with-css)