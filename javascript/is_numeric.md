# Check if a string is a valid number

```javascript
var str = '25.99';
var is_numeric = (typeof str == 'string') && !isNaN(parseFloat(str));
         
```

- var str - declare test string with number
- typeof str == 'string' - ensure ```str``` is of ```string``` type
- isNaN(parseFloat(str)) - ensure ```str``` contains valid number
