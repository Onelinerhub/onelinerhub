# How do I use jQuery to execute code when the window has finished loading?
// plain

To execute code when the window has finished loading, you can use the jQuery `$(window).load()` function. This function takes in a function as an argument which will be executed when the window has finished loading. For example:

```
$(window).load(function() {
    alert("The window has finished loading!");
});
```

## Output example


```
An alert box with the message "The window has finished loading!"
```

## Code explanation

- `$(window).load()`: the jQuery function to execute code when the window has finished loading
- `function() { ... }`: the function to be executed when the window has finished loading
- `alert("The window has finished loading!");`: the code to be executed when the window has finished loading

## Helpful links
- [jQuery API Documentation - $(window).load()](https://api.jquery.com/load/)

onelinerhub: [How do I use jQuery to execute code when the window has finished loading?](https://onelinerhub.com/jquery/how-do-i-use-jquery-to-execute-code-when-the-window-has-finished-loading)