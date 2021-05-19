# Create array with N random elements (1...N range)

```javascript
var arr = new Array(10);
for ( var i = 0; i < arr.length; i++) arr[i] = Math.round(50 + Math.random() * 25);
```

- var arr = new Array(10) - declares new array with ```10``` elements
- 50 - random range will start from ```50```
- 25 - random range will end with ```75``` (```50 + 25```)
- Math.round(50 + Math.random() * 25) - generate random integer

group: ranges
