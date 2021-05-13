# Store object to localStorage

```javascript
var obj = { a: 1, b: 2 };
localStorage.setItem('obj', JSON.stringify(obj));
```

- var obj - declare test object
- localStorage.setItem - saves item to localStorage (should be of String type)
- JSON.stringify(obj) - converts our ```obj``` object to JSON string

group: local_storage
