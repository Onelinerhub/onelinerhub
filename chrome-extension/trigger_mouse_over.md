# How to simulate mouse over event on a page

```javascript
document.querySelector('div')
.dispatchEvent( new MouseEvent('mouseover', {'bubbles': true})) ;
```

- `'div'` - query selector for an element to simulate mouse over on
- `dispatchEvent` - triggers specified event
- `MouseEvent` - creates specified mouse event
- `mouseover` - we need to simulate mouse over
- `{'bubbles': true}` - event will bubble up the hierarchy of the elements (standard mouseover behaviour)

group: trigger_event


link_youtube: https://youtu.be/-Ha40WJldBo
