# Scroll to a specific element

```javascript
$('body').animate({ scrollTop: $('#element').offset().top }, 2 * 1000);
```

- $('body') - selects document body
- animate - animates given properties
- '#element' - selector for an element we want to scroll to
- .offset().top - get Y coordinate for the given element
- 2 * 1000 - will animate scroll for 2 seconds
