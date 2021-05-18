# Get unique values from array

```javascript
var arr = [1, 2, 3, 2, 4];
var unique = arr.filter(function(val, i, self) { return self.indexOf(val) === i; });
```

- var arr - declare array with duplicate elements
- var unique - will contain final array with unique values only
- arr.filter - filter allows iterating through array with a custom function
- return self.indexOf(val) === i - custom function will return ```false``` (value will be removed from final array) if current element is duplicate
