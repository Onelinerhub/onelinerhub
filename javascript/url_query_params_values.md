# Get URL query string values by name

```javascript
var value = (new URLSearchParams(window.location.search)).get('param');
```

- var value - this variable will contain value of specified query param
- new URLSearchParams - creates object that parses query string
- window.location.search - query string part of current url
- get('param') - get value for query string parameter named ```param```
