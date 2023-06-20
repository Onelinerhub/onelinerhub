# How do I use d3.js to perform an action when a user clicks on an element?
// plain

Using d3.js, you can perform an action when a user clicks on an element by using the `on` method. This method takes two arguments, the first being the type of event (in this case, `click`), and the second being a callback function to run when the event occurs.

For example, if you wanted to log a message to the console when a user clicks on an element with the ID of "example":

```javascript
d3.select("#example").on("click", function() {
  console.log("User clicked on element!");
});
```

This code will cause the message "User clicked on element!" to be logged to the console when the element with the ID of "example" is clicked.

The parts of this code are as follows:

* `d3.select("#example")` - this selects the element with the ID of "example" from the DOM
* `.on("click", function() { ... })` - this adds an event listener for the "click" event, and runs the callback function when the event occurs
* `console.log("User clicked on element!")` - this logs the message "User clicked on element!" to the console

For more information, see the [d3.js documentation](https://github.com/d3/d3/blob/master/API.md#selections-on).

onelinerhub: [How do I use d3.js to perform an action when a user clicks on an element?](https://onelinerhub.com/javascript-d3/how-do-i-use-d--js-to-perform-an-action-when-a-user-clicks-on-an-element)