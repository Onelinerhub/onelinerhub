# Break each() function loop

```javascript
$('div').each(function() {
  if ( $(this).hasClass('.error') ) return false;
});
```

- 'div' - elements selector to loop through (all ```div```s in our case)
- each( - loop through all found elements
- $(this).hasClass('.error') - condition to break the loop
- return false - if we return false, ```each()``` will stop iterating
