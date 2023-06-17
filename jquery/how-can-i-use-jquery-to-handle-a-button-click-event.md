# How can I use jQuery to handle a button click event?
// plain

Using jQuery, you can easily handle a button click event. Here is an example code block demonstrating how to do that:

```
$("button").click(function(){
    alert("Button was clicked!");
});
```
When the button is clicked, an alert message will be displayed:
```
Button was clicked!
```

The code is composed of the following parts:
1. `$("button")` - Selects the button element.
2. `click()` - Attaches a click event handler to the button element.
3. `function(){ ... }` - A callback function to execute when the button is clicked.
4. `alert("Button was clicked!")` - Displays an alert message when the button is clicked.

For more information about jQuery click events, please refer to the following links:
- [jQuery Click Event](https://api.jquery.com/click/)
- [jQuery .on()](https://api.jquery.com/on/)

onelinerhub: [How can I use jQuery to handle a button click event?](https://onelinerhub.com/jquery/how-can-i-use-jquery-to-handle-a-button-click-event)