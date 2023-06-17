# How do I use jQuery to zoom in on an image?
// plain

To use jQuery to zoom in on an image, you can leverage the jQuery animate() function. The animate() function will allow you to set the size of an image to a larger size over a specified duration. This will create a zoom in effect.

The following example code will zoom in on an image over the course of 1 second:

```
$("#myImage").animate({
    width: "500px",
    height: "500px"
}, 1000);
```

The code above will set the width and height of the element with the ID `#myImage` to 500px over the course of 1 second (1000 milliseconds).

## Code explanation


* `$("#myImage")` - A jQuery selector for the element with the ID `#myImage`
* `animate({...})` - The jQuery animate() function, which takes an object of properties to animate over a specified duration
* `width: "500px"` - The width property to animate to 500px
* `height: "500px"` - The height property to animate to 500px
* `1000` - The duration of the animation in milliseconds

## Helpful links

* [jQuery animate()](https://api.jquery.com/animate/)

onelinerhub: [How do I use jQuery to zoom in on an image?](https://onelinerhub.com/jquery/how-do-i-use-jquery-to-zoom-in-on-an-image)