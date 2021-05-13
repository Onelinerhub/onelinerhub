# Format date in HH:II (hours:minutes)

```javascript
var d = new Date();
var formatted = ('0' + d.getHours()).slice(-2) + ':' + ('0' + d.getMinutes()).slice(-2);
```

- var d = new Date() - create date object
- d.getHours() - returns current hour
- d.getMinutes() - returns current minute

group: date_format
