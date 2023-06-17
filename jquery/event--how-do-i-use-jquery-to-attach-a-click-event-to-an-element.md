# event

How do I use jQuery to attach a click event to an element?
// plain

jQuery provides a simple way to attach a click event to an element. To do this, you can use the `.on()` method. This method takes two parameters: the event type, and a callback function to execute when the event occurs.

For example, the following code will attach a click event to the element with the ID of `example`:
```javascript
$('#example').on('click', function(event) {
    // do something
});
```

The code above will attach a click event to the element with the ID of `example`. When the element is clicked, the callback function will execute. This function takes an `event` parameter, which can be used to access information about the event.

For more information, see the [jQuery documentation for `.on()`](https://api.jquery.com/on/).

onelinerhub: [event

How do I use jQuery to attach a click event to an element?](https://onelinerhub.com/jquery/event--how-do-i-use-jquery-to-attach-a-click-event-to-an-element)