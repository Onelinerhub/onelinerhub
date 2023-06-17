# How do I use jQuery to trigger an action on hover?
// plain

Using jQuery, you can trigger an action on hover by using the `.hover()` method. This method takes two functions as parameters, the first is the action that will be triggered on mouseover, and the second is the action that will be triggered on mouseout.

For example, this code will change the background color of an element with the id of `example` to yellow on mouseover, and back to white on mouseout:

```javascript
$("#example").hover(
  function(){
    $(this).css("background-color", "yellow");
  },
  function(){
    $(this).css("background-color", "white");
  }
);
```

The code consists of the following parts:

* `$("#example")` - Selects the element with the id of `example`.
* `.hover()` - The hover method.
* `function(){ $(this).css("background-color", "yellow"); }` - The first function, which is triggered on mouseover and changes the background color to yellow.
* `function(){ $(this).css("background-color", "white"); }` - The second function, which is triggered on mouseout and changes the background color back to white.

## Helpful links

* [jQuery .hover() Documentation](https://api.jquery.com/hover/)
* [jQuery .css() Documentation](https://api.jquery.com/css/)

onelinerhub: [How do I use jQuery to trigger an action on hover?](https://onelinerhub.com/jquery/how-do-i-use-jquery-to-trigger-an-action-on-hover)