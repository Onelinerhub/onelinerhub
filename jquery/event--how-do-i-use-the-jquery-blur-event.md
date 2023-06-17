# event

How do I use the jQuery blur event?
// plain

The jQuery blur event is triggered when an element loses focus. The blur event can be used to validate user input or to trigger a certain action when a user leaves an element.

## Example code

```
$("#inputField").blur(function(){
    alert("Input field lost focus!");
});
```

## Output example

```
Alert message: Input field lost focus!
```

The code above will trigger an alert message when the input field loses focus.

## Code explanation

- `$("#inputField")` - selects the element with the id "inputField"
- `.blur(function(){` - triggers the blur event
- `alert("Input field lost focus!");` - displays an alert message when the blur event is triggered
- `});` - closes the function

## Helpful links
- [jQuery blur event](https://api.jquery.com/blur/)
- [jQuery Events](https://api.jquery.com/category/events/)

onelinerhub: [event

How do I use the jQuery blur event?](https://onelinerhub.com/jquery/event--how-do-i-use-the-jquery-blur-event)