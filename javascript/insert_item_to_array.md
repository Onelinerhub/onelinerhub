# Insert an item to an array at a certain index

```javascript
var arr = ['value1', 'value2'];
arr.splice(1, 0, 'new value');
```

- var arr - declare test array to insert new value into
- arr.splice - inserts a new value into an array
- (1, - index to insert new value at (starts at ```0```, so we will insert our value at second position)
- 0, - do not delete any values from old array
- 'new value' - what value to insert
