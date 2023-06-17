# How can I use jQuery to detect a change in an element?
// plain

jQuery provides a convenient way to detect changes in an element using the `.on()` method. This method takes three parameters: the event type, the element to be monitored, and a callback function.

The event type can be any of the events that jQuery supports, such as `change`, `click`, `keyup`, etc. The element to be monitored is the element that will be checked for changes. The callback function is the function that will be executed when the element changes.

For example, to detect a change in an `<input>` element, you could use the following code:

```javascript
$('input').on('change', function() {
    // code to be executed when input changes
});
```

The code above will execute the callback function whenever the `<input>` element changes.

You can also use the `.on()` method to detect changes in multiple elements at the same time. For example, to detect a change in both an `<input>` and a `<select>` element, you could use the following code:

```javascript
$('input, select').on('change', function() {
    // code to be executed when input or select changes
});
```

The code above will execute the callback function whenever either the `<input>` or the `<select>` element changes.

## Helpful links

- [jQuery .on() Method](https://api.jquery.com/on/)
- [jQuery Events](https://api.jquery.com/category/events/)

onelinerhub: [How can I use jQuery to detect a change in an element?](https://onelinerhub.com/jquery/how-can-i-use-jquery-to-detect-a-change-in-an-element)