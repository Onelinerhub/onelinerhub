# How to check if an object is empty

```javascript
var o = {}
var is_empty = Object.keys(o).length === 0
```

- var o - defines test empty object
- var is_empty - this variable will contain ```true``` if the object is empty
- Object.keys(o).length - this will return the length of an array with keys of an ```o``` object
