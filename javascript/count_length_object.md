# Count number of elements in object (length of object)

```javascript
var obj = {a: 1, b: 2};
var size = 0;
for ( k in obj ) size++;
console.log(size);
```

- var obj - declares test object
- for ( k in obj ) size++ - iterates through object and counts all properties
- console.log(size) - replace with your code to operate with ```size``` of ```obj```
