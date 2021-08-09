# Get unique values from array

```javascript
var list = [1, 2, 3, 4, 5, 5];
var unique = [...new Set(list)];
```

- var list - declare test array to get unique values from
- new Set(list) - store unique values from passed `list` array (can contain objects of any type, from primitive values to object references).
