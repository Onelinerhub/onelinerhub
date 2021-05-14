# Check if variable is a string

```javascript
var str = new String('Hi');
var is_string = (typeof str === 'string' || str instanceof String);
```

- var str = new String('Hi'); - declare test string in an object manner
- typeof str === 'string' - checks if ```str``` is a plain string
- str instanceof String - checks if ```str``` is an object of ```String``` type
- is_string - will contain ```true``` if ```str``` is either a plain string or an object string
