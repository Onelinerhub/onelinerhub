# How do I use the jQuery keypress enter event?
// plain

The jQuery keypress enter event can be used to trigger a function when the enter key is pressed. To use this event, you must first bind the event to an element using the `.on()` method. The syntax for this is as follows:

```
$(selector).on('keypress', function(e){
    // code to execute
});
```

In this example, `selector` is the element that the event will be bound to, and `e` is the event object. Inside the function, you can check for the enter key using the `.which` property of the event object. If the enter key is pressed, the value of `e.which` will be 13.

```
$('input').on('keypress', function(e){
    if(e.which == 13){
        // enter key was pressed
    }
});
```

In this example, the enter key press event is bound to an `input` element. If the enter key is pressed, the code inside the `if` statement will be executed.

You can also use the `.keypress()` method instead of the `.on()` method. The syntax for this is as follows:

```
$(selector).keypress(function(e){
    // code to execute
});
```

This is a shorthand version of the `.on()` method.

## Helpful links

- [jQuery .on() Method](https://api.jquery.com/on/)
- [jQuery .keypress() Method](https://api.jquery.com/keypress/)

onelinerhub: [How do I use the jQuery keypress enter event?](https://onelinerhub.com/jquery/how-do-i-use-the-jquery-keypress-enter-event)