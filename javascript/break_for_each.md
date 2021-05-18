# How to break Array.forEach

```javascript
var arr = [1, 2, 3, 4, 5];

try {
  arr.forEach(function(v) {
    // process v
    if (v === 3) throw new Error('stop');
  });
} catch (e) {
 if ( e.message != 'stop' ) throw e;
}
```

- var arr - array to iterate through
- process v - replace with your code that manipulates on array elements
- if (v === 3) - we will break after element with value ```3```
- throw new Error('stop') - in order to break we throw Error with ```stop``` message
- if ( e.message != 'stop' ) throw e - if this is not our error, throw it further
