# Generate random integer number within specified range

```javascript
var from = 10;
var to = 20;
Math.round(Math.random() * (to - from)) + from;
```

- var from - range starting with this number
- var to - range ending with thin number
- Math.random() - will generate random float within ```0...1```
- Math.round - will round random result to get integer number

group: random_generate
