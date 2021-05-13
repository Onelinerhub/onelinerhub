# Pretty print JSON

```javascript
var obj = {a: 1, b: 2};
console.log( JSON.stringify(obj, null, 2) );
```

- var obj - declare test object to print
- JSON.stringify - convert JSON to string ([docs](https://developer.mozilla.org/ru/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify))
- , 2) - will format JSON with 2-spaces indents
