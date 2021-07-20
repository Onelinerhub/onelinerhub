# Confirm page close action

```javascript
window.onbeforeunload = function(e) { return true; }
```

- onbeforeunload - event that fires before page is closed
- return true - function can only return values, since browser only allows confirming closing the page
