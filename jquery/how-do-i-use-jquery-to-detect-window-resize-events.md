# How do I use jQuery to detect window resize events?
// plain

jQuery provides a `resize()` event for detecting when the browser window has been resized. The `resize()` event can be used on any element, but is most often used on the `window` object.

Below is an example of using the `resize()` event on the `window` object.

```javascript
$(window).resize(function() {
  console.log('Window was resized');
});
```

When this code is run, the message `Window was resized` will be logged to the console every time the browser window is resized.

## Code explanation


1. `$(window)` - This is a jQuery selector used to select the window object.
2. `.resize()` - This is a jQuery method used to bind an event handler to the `resize` event.
3. `function()` - This is the event handler function that will be called when the `resize` event is triggered.
4. `console.log('Window was resized')` - This is the code that will be executed when the `resize` event is triggered.

## Helpful links

- [jQuery resize() event](https://api.jquery.com/resize/)

onelinerhub: [How do I use jQuery to detect window resize events?](https://onelinerhub.com/jquery/how-do-i-use-jquery-to-detect-window-resize-events)