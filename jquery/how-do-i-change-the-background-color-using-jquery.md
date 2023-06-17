# How do I change the background color using jQuery?
// plain

To change the background color of an element using jQuery, you can use the `.css()` method. This method takes two parameters, the first being the property to change and the second being the value of the property. For example, to change the background color of an element with the id 'myElement' to red, you can use the following code:

```
$('#myElement').css('background-color', 'red');
```

This will set the background color of the element with the id 'myElement' to red.

The `.css()` method can also be used to change multiple properties at once. To do this, you can pass an object to the `.css()` method with the property names as keys and the values as the corresponding values. For example, to change the background color of the element with the id 'myElement' to red and the font color to white, you can use the following code:

```
$('#myElement').css({
    'background-color': 'red',
    'color': 'white'
});
```

This will set the background color of the element with the id 'myElement' to red and the font color to white.

## Helpful links
- [jQuery .css() Method](https://api.jquery.com/css/)

onelinerhub: [How do I change the background color using jQuery?](https://onelinerhub.com/jquery/how-do-i-change-the-background-color-using-jquery)