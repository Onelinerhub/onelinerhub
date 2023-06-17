# How do I use jQuery to add a click event to an element?
// plain

To use jQuery to add a click event to an element, you can use the `.click()` method. This method takes an optional parameter which is a function that will be executed when the element is clicked. For example:

```javascript
$("button").click(function(){
    alert("Button was clicked!");
});
```

This code will cause an alert to be displayed when the button is clicked.

The code can be broken down as follows:

* `$("button")`: This selects the `<button>` element on the page.
* `.click()`: This adds an event listener to the element, which will be triggered when the element is clicked.
* `function(){...}`: This is the function that will be executed when the element is clicked.

## Helpful links
* [jQuery API Documentation - .click()](https://api.jquery.com/click/)

onelinerhub: [How do I use jQuery to add a click event to an element?](https://onelinerhub.com/jquery/how-do-i-use-jquery-to-add-a-click-event-to-an-element)