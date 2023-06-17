# How do I disable a button using jQuery?
// plain

To disable a button using jQuery, you can use the `prop()` method. This method sets or returns properties and values of the selected elements. To disable a button, you can set the `disabled` property to `true`.

```
$(document).ready(function(){
  $("button").click(function(){
    $(this).prop("disabled", true);
  });
});
```

The code above will disable the button when it is clicked.

The parts of the code are:

- `$(document).ready(function(){`: This is a jQuery method which allows the code to execute when the DOM is fully loaded.
- `$("button")`: This is a jQuery selector which selects all the `<button>` elements in the DOM.
- `.click(function(){`: This is a jQuery method which allows you to add an event listener to the selected elements.
- `$(this)`: This is a jQuery selector which selects the current element.
- `.prop("disabled", true)`: This is a jQuery method which sets the `disabled` property of the selected element to `true`.

## Helpful links
- [jQuery prop() Method](https://www.w3schools.com/jquery/jquery_dom_set.asp)
- [jQuery click() Method](https://www.w3schools.com/jquery/jquery_events.asp)

onelinerhub: [How do I disable a button using jQuery?](https://onelinerhub.com/jquery/how-do-i-disable-a-button-using-jquery)