# How do I use the jQuery window load function?
// plain

The jQuery window load function is used to execute code after the page has finished loading. This can be useful for making sure that all of the content on the page is available before the code is executed.

## Example code

```
$(window).load(function(){
  alert("Page has finished loading!");
});
```
## Output example

```
Page has finished loading!
```

## Code explanation

- `$(window)` - This is a jQuery selector that selects the window object.
- `.load(function(){...})` - This is a jQuery method that executes the function passed as an argument after the page has finished loading.
- `alert("Page has finished loading!");` - This is a JavaScript method that displays an alert message to the user.

## Helpful links
- [jQuery window load documentation](https://api.jquery.com/load/)

onelinerhub: [How do I use the jQuery window load function?](https://onelinerhub.com/jquery/how-do-i-use-the-jquery-window-load-function)