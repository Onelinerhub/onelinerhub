# How do I use jQuery to trigger an event?
// plain

jQuery provides a convenient way to trigger an event using the `trigger()` method. This method can be used to trigger any event that is bound to an element.

## Example code

```javascript
$('#myButton').on('click', function() {
  alert('Button was clicked');
});

$('#myButton').trigger('click');
```
## Output example

`Button was clicked`

## Code explanation

1. `$('#myButton')` - This is the jQuery selector used to select the element with the id `myButton`.
2. `on('click', function() { ... })` - This is the event handler that is bound to the element when it is clicked.
3. `alert('Button was clicked')` - This is the code that will be executed when the element is clicked.
4. `trigger('click')` - This is the method used to trigger the event bound to the element.

## Helpful links
- [jQuery trigger() Method](https://www.w3schools.com/jquery/event_trigger.asp)

onelinerhub: [How do I use jQuery to trigger an event?](https://onelinerhub.com/jquery/how-do-i-use-jquery-to-trigger-an-event)