# Get random element from array

```javascript
var arr = [1, 2, 3];
var random = arr[ Math.floor(Math.random() * arr.length) ];
```

- var arr - declare test array
- var random - this variable will contain resulting random element from an array
- Math.floor - will return lower closest integer for the specified float number
- Math.random - returns random float from ```0``` to ```1```
