# How do I use jQuery to scroll to a specific element on a page?
// plain

To use jQuery to scroll to a specific element on a page, the following code can be used:

```
$('html, body').animate({
    scrollTop: $("#target-element").offset().top
}, 1000);
```
This code will animate the scroll position of the page to the top of the element with the ID of "target-element" over the course of 1 second (1000 milliseconds).

The code can be broken down into the following parts:

- `$('html, body')`: This selects the `html` and `body` elements, which are the main parent elements of the page.
- `animate()`: This is a jQuery method which animates the properties of the selected elements.
- `scrollTop`: This is the property of the `html` and `body` elements which is being animated.
- `$("#target-element")`: This selects the element with the ID of "target-element".
- `offset()`: This is a jQuery method which returns the current coordinates of the selected element relative to the document.
- `top`: This is the top coordinate of the element.
- `1000`: This is the duration of the animation in milliseconds.

## Helpful links
- [jQuery animate()](https://api.jquery.com/animate/)
- [jQuery offset()](https://api.jquery.com/offset/)

onelinerhub: [How do I use jQuery to scroll to a specific element on a page?](https://onelinerhub.com/jquery/how-do-i-use-jquery-to-scroll-to-a-specific-element-on-a-page)