# Detect pressing Enter

```javascript
$(document).on('keypress', function(e) {
  if ( e.which == 13 ) console.log('Enter pressed');
});
```

- $(document).on('keypress' - attach keypress event to document
- e.which == 13 - check if ```Enter``` key was pressed
- console.log('Enter pressed') - replace with your code to fire on Enter pressed

group: press_specific_key
