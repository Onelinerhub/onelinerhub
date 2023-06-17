# event

How can I use jQuery's live event feature?
// plain

jQuery's `live` event feature allows you to attach an event handler to elements that are added to the DOM after the page has loaded. This feature is useful when you have dynamic content that is added after the page has loaded and you need to attach an event handler to it.

## Example code

```javascript
$('a.myLink').live('click', function() {
  alert('Link clicked!');
});
```

## Output example

`Link clicked!`

## Code explanation

- `$('a.myLink')`: Selects all `<a>` elements with the class `myLink`.
- `live('click', function() { ... })`: Attaches a `click` event handler to the selected elements, which will be triggered when the element is clicked.
- `alert('Link clicked!')`: Displays an alert message when the element is clicked.

## Helpful links
- https://api.jquery.com/live/
- https://www.w3schools.com/jquery/event_live.asp

onelinerhub: [event

How can I use jQuery's live event feature?](https://onelinerhub.com/jquery/event--how-can-i-use-jquery-s-live-event-feature)