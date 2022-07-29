# Add single handler to multiple events

```javascript
$('input').on('click focus keydown', function(e) {
  console.log('hey!');
});
```

- `'input'` - selector for needed element to bind events to
- `.on(` - binds event handlers to specified events
- `click focus keydown` - list of events to bind handler to
- `console.log('hey!');` - replace with your code to handle specified events


link_youtube: https://youtu.be/2IIzDcx3y8U
