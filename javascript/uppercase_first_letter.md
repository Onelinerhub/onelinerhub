# Uppercase first letter

```javascript
var str = 'this is a text';
var result = str.substr(0, 1).toUpperCase() + str.substr(1);
```

- var str - define test string
- substr(0, 1).toUpperCase() - capitalizes first symbol of a string
- str.substr(1) - concatenates everything else but first symbol
- var result - this variable will contain resulting string
