# How do I use jQuery to detect keycodes?
// plain

### Answer

Using jQuery, you can detect keycodes by binding a keydown event to the document, and then using the `event.which` property to get the keycode of the pressed key.

```javascript
$(document).keydown(function(event) {
    var keycode = event.which;
    console.log(keycode);
});
```

This code will output the keycode of the key pressed in the console.

## Code explanation


1. `$(document).keydown(function(event)` - Binds a keydown event to the document
2. `var keycode = event.which` - Gets the keycode of the pressed key from the event object
3. `console.log(keycode)` - Outputs the keycode to the console

## Helpful links

- [jQuery keydown() Method](https://www.w3schools.com/jquery/event_keydown.asp)
- [JavaScript Event Object](https://www.w3schools.com/jsref/obj_event.asp)

onelinerhub: [How do I use jQuery to detect keycodes?](https://onelinerhub.com/jquery/how-do-i-use-jquery-to-detect-keycodes)