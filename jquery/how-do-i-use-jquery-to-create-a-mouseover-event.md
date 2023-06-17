# How do I use jQuery to create a mouseover event?
// plain

To use jQuery to create a mouseover event, you can use the `.hover()` method. This method takes two functions as parameters, the first for the `mouseover` event and the second for the `mouseout` event.

For example:
```
$("#example").hover(
  function(){
    alert("You entered #example!");
  },
  function(){
    alert("Bye! You now leave #example");
  }
);
```

When the mouse hovers over the element with the id `example`, an alert message will appear saying "You entered #example!" and when the mouse moves out of the element, an alert message will appear saying "Bye! You now leave #example".

The parts of the code are:
- `$("#example")`: This is a jQuery selector which selects the element with the id `example`.
- `.hover()`: This is a jQuery method which takes two functions as parameters.
- `function(){}`: This is an anonymous function which contains the code that will be executed when the event is triggered.
- `alert("You entered #example!");`: This is an example of code which will be executed when the mouse hovers over the element.

## Helpful links
- [jQuery Hover](https://api.jquery.com/hover/)
- [jQuery Selectors](https://api.jquery.com/category/selectors/)

onelinerhub: [How do I use jQuery to create a mouseover event?](https://onelinerhub.com/jquery/how-do-i-use-jquery-to-create-a-mouseover-event)