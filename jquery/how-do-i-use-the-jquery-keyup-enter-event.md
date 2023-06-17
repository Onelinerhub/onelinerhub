# How do I use the jQuery keyup enter event?
// plain

The jQuery `keyup()` event is used to detect when a key is released on the keyboard. The `enter` key is commonly used to submit forms or trigger a search. To use the `keyup()` event with the `enter` key, you can use the following code:

```
$('input').keyup(function(e) {
    if (e.keyCode == 13) {
        // Do something when enter is pressed
    }
});
```

The `keyup()` event takes a function as a parameter which will be called when a key is released. Inside the function, the `keyCode` of the key that was released is checked. If the `keyCode` is `13`, then the `enter` key was pressed.

The following are the parts of the code:

1. `$('input').keyup(function(e)` - This part of the code attaches the `keyup()` event to all `<input>` elements. The event will call the function passed to it whenever a key is released.

2. `if (e.keyCode == 13)` - This part of the code checks if the `keyCode` of the key that was released is `13`. If it is, then the `enter` key was pressed.

3. `// Do something when enter is pressed` - This part of the code will be executed if the `enter` key was pressed.

## Helpful links

- [jQuery keyup()](https://api.jquery.com/keyup/)
- [KeyboardEvent.keyCode](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/keyCode)

onelinerhub: [How do I use the jQuery keyup enter event?](https://onelinerhub.com/jquery/how-do-i-use-the-jquery-keyup-enter-event)