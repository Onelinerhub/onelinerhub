# Detect pressing Esc

```javascript
$(document).on('keypress', function(e) {
  if ( e.which == 27 ) console.log('Esc pressed');
});
```

- $(document).on('keypress' - attach keypress event to document
- e.which == 27 - check if ```Esc``` key was pressed
- console.log('Esc pressed') - replace with your code to fire on Esc pressed

group: press_specific_key
