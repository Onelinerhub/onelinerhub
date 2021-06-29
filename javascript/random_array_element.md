# Get random element from array

```javascript
arr[ Math.floor(Math.random() * arr.length) ]
```

- arr - array to get random element from
- Math.floor - will return lower closest integer for the specified float number
- Math.random - returns random float from ```0``` to ```1```

## Example
```javascript
var arr = [1, 2, 3];
var random = arr[ Math.floor(Math.random() * arr.length) ];
```
```javascript
2
```
