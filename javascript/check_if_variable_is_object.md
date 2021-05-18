# Check if variable is an object

```javascript
var obj = {};
var is_object = typeof obj === 'object' && obj !== null;
```

- var obj = {} - declare test object
- is_object - will contain ```true``` if ```obj``` is object
- typeof obj === 'object' - ensure type of ```obj``` is ```object```
- obj !== null - ensure our variable is not ```null``` (because of ```typeof null``` = ```'object'```)

group: check_variable_type
