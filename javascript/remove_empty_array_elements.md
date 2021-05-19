# Remove empty elements from an array

```javascript
var arr = [1, 2, 3, null, , , undefined, 4, 5, ''];
var clean = arr.filter(function (v) { return v != null && v != ''; });
```

- var arr - declare test array with several empty elements to remove
- clean - will contain resulting array with non-empty values only
- return v != null && v != '' - remove null/undefined and empty strings from array
