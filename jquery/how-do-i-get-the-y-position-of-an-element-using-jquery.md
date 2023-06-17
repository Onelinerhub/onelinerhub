# How do I get the y-position of an element using jQuery?
// plain

In order to get the y-position of an element using jQuery, you can use the `offset()` method. This method returns an object containing the properties `top` and `left`, which represent the distance of the element relative to the offset parent.

## Example code

```
var yPosition = $('#myElement').offset().top;
```

The code above will set the variable `yPosition` to the y-position of the element with the id `myElement`.

## Code explanation

- `$('#myElement')` - This will select the element with the id `myElement`.
- `offset()` - This method will return an object containing the properties `top` and `left`.
- `.top` - This property will return the distance of the element relative to the offset parent in the y-axis.

## Helpful links
- [jQuery offset() method](https://api.jquery.com/offset/)

onelinerhub: [How do I get the y-position of an element using jQuery?](https://onelinerhub.com/jquery/how-do-i-get-the-y-position-of-an-element-using-jquery)