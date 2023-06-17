# How do I add a jQuery event listener to my webpage?
// plain

To add a jQuery event listener to a webpage, you can use the `.on()` method. This method attaches event handlers to the selected elements and their child elements.

For example, the following code will attach a click event handler to all `<p>` elements on the page:
```javascript
$("p").on("click", function(){
    alert("You clicked a paragraph!");
});
```
When a user clicks on a `<p>` element, an alert message will appear.

The `.on()` method takes two arguments:
1. The event type as a string (e.g. "click", "mouseover", etc.)
2. A callback function that will be executed when the event is triggered.

Here are some useful resources for learning more about the `.on()` method:
* [jQuery API Documentation](https://api.jquery.com/on/)
* [jQuery Event Basics](https://learn.jquery.com/events/event-basics/)

onelinerhub: [How do I add a jQuery event listener to my webpage?](https://onelinerhub.com/jquery/how-do-i-add-a-jquery-event-listener-to-my-webpage)