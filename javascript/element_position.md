# How to get element position relative to window

```javascript
var pos = document.querySelector('#id').getBoundingClientRect();
var x = pos.left;
var y = pos.top;
```

- document.querySelector('#id') - element selector to get position of
- getBoundingClientRect() - returns top/left/right/bottom coordinates of an element relative to the browser window
- var x - will contain left coordinate
- var y - will contain top coordinate
