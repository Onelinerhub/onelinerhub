# Find index of array element with a certain value

```javascript
arr.findIndex(el => el == 'val')
```

- arr - array to search in
- findIndex - find index of the element defined by a callback function
- el == 'val' - we want to get index of an element with `val` value


## Example
```javascript
var arr = ['oh', 'hi', 'ha'];
var index = arr.findIndex(el => el == 'hi');
console.log(index);
```
```
1
```
