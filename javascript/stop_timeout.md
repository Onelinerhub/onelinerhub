# How to stop setTimeout execution

```javascript
var timeout = setTimeout(function() {}, 1000);
clearTimeout(timeout);
```

- var timeout - stores timeout ID
- setTimeout(function() {}, 1000) - declare test timeout call of some function
- clearTimeout(timeout) - stop previously launched timeout by ID

group: timeouts
