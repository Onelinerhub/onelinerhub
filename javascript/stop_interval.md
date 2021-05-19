# How to stop setInterval execution

```javascript
var interval = setInterval(function() {}, 1000);
clearInterval(interval);
```

- var interval - stores interval ID
- setInterval(function() {}, 1000) - declare test interval call of a function every second
- clearInterval(interval) - stop previously launched interval by ID

group: timeouts
