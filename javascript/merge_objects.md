# How to merge properties of 2 objects

```javascript
let o1 = {a: 1};
let o2 = {b: 2};
let res = {...o1, ...o2};
```

- let o1 - declare first test object
- let o2 - declare second test object
- let res - will contain merged object
- ... - object [spread operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax)
